from enum import Enum
from os import path, makedirs
from shutil import rmtree
from pickle import dump, load
from time import sleep
from traceback import format_exc
from uuid import uuid4

from PyQt5 import QtCore

import socialreaper
from socialreaper import IterError

from components.globals import *


def _api_error_hint(error):
    message = str(error).lower()
    hints = []

    if any(
        token in message
        for token in (
            "unauthorized",
            "forbidden",
            "invalid token",
            "access token",
            "oauth",
            "401",
            "403",
            "bad authentication data",
        )
    ):
        hints.append(
            "Credentials appear invalid or expired. Re-check API keys for this source."
        )

    if any(
        token in message
        for token in ("deprecated", "unsupported", "endpoint", "410", "removed")
    ):
        hints.append(
            "The provider endpoint may be deprecated or changed. Verify current API docs."
        )

    if not hints:
        return None

    return " ".join(hints)


class QueueState(Enum):
    RUNNING = "running"
    STOPPED = "stopped"


class JobState(Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    QUEUED = "queued"
    SAVING = "saving"
    FINISHED = "finished"


class JobData:

    def __init__(self, cache=True):
        self.MAX_ROWS = 1000

        self.cache_enabled = cache
        self.location = path.join(CACHE_DIR, str(uuid4()))
        self.cache_count = 0
        self.failed = False

        self.data = []
        self.keys = set()
        self.count = 0

    def add_row(self, row):
        flat_data = socialreaper.tools.flatten(row)
        self.data.append(flat_data)

        self.count += 1

        keys = flat_data.keys()
        if keys != self.keys:
            self.keys.update(keys)

        if self.cache_enabled:
            self.cache()

    def cache(self):
        if self.failed or (self.count % self.MAX_ROWS != 0):
            return
        else:
            if self.cache_count == 0:
                try:
                    makedirs(self.location)
                except OSError:
                    self.failed = True
                    return

            location = path.join(self.location, str(self.cache_count))
            try:
                with open(location, "wb") as f:
                    dump(self.data, f)
                    self.data = []
                    self.cache_count += 1
            except IOError:
                self.failed = True

    def read(self):
        return self.JobDataIter(self)

    class JobDataIter:

        def __init__(self, job_data):
            self.job_data = job_data
            self.cache_count = 0
            self.finished_cache = False

            self.data = []
            self.i = 0

        def __iter__(self):
            return self

        def read_cache_i(self, i):
            location = path.join(self.job_data.location, str(i))

            try:
                with open(location, "rb") as f:
                    self.data = load(f)
                    self.i = 0
                    self.cache_count += 1
            except IOError as e:
                print(e)
                raise e

        def read_memory(self):
            self.data = self.job_data.data
            self.i = 0
            self.finished_cache = True

        def read_row(self):
            row = self.data[self.i]
            self.i += 1

            for key in self.job_data.keys:
                if not row.get(key):
                    row[key] = ""

            return row

        def clean_up(self):
            rmtree(self.job_data.location, ignore_errors=True)

        def __next__(self):
            if not self.finished_cache:
                if (
                    self.cache_count <= self.job_data.cache_count
                ) and self.job_data.cache_count != 0:
                    if self.i < len(self.data):
                        return self.read_row()
                    else:
                        if self.cache_count == self.job_data.cache_count:
                            self.cache_count += 1
                        else:
                            self.read_cache_i(self.cache_count)
                        return self.__next__()
                else:
                    self.read_memory()
                    return self.__next__()
            else:
                if self.i < len(self.data):
                    return self.read_row()
                else:
                    self.clean_up()
                    raise StopIteration


class Job:
    error_log = QtCore.pyqtSignal(str)

    def __init__(
        self,
        outputPath,
        sourceName,
        sourceFunction,
        functionArgs,
        sourceKeys,
        append,
        keyColumn,
        encoding,
        cache,
        job_update,
        job_error_log,
    ):
        self.source = eval(f"socialreaper.{sourceName}(**{sourceKeys})")
        self.source.api.log_function = self.log
        self.log_function = job_error_log
        self.error = None

        self.iterator = eval(f"self.source.{sourceFunction}({functionArgs})")
        self.outputPath = outputPath
        self.sourceName = sourceName
        self.sourceFunction = sourceFunction
        self.functionArgs = functionArgs
        self.sourceKeys = sourceKeys

        self.append = append
        self.keyColumn = keyColumn
        self.encoding = encoding
        self.cache = cache

        self.state = JobState.STOPPED
        self.job_update = job_update
        self.log_data = ""
        self.data = JobData(cache)

    def log(self, string):
        self.log_function.emit(str(string))

    def inc_data(self):
        self.state = JobState.RUNNING
        try:
            value = next(self.iterator)
            self.data.add_row(value)
            self.job_update.emit(self)
            return value
        except StopIteration:
            try:
                return self.end_job()
            except Exception as e:
                self.log(format_exc())
        except IterError as e:
            self.error = e
            raise e

    def end_job(self):
        self.state = JobState.SAVING
        self.job_update.emit(self)
        socialreaper.tools.CSV(
            self.data.read(),
            file_name=self.outputPath,
            flat=False,
            append=self.append,
            key_column=self.keyColumn,
            encoding=self.encoding,
            fill_gaps=False,
            field_names=sorted(self.data.keys),
        )
        self.state = JobState.FINISHED
        self.job_update.emit(self)
        return False

    def send_update(self):
        if self.state == JobState.RUNNING:
            if self.iterator.total % 20:
                self.job_update.emit(self)
            else:
                return

        self.job_update.emit(self)

    def pickle(self):
        self.log_function = None
        self.job_update = None

        dir = LOG_DIR

        if not path.exists(dir):
            makedirs(dir)

        with open(f"{dir}/out.pickle", "wb") as f:
            dump(self, f)


class Queue(QtCore.QThread):
    job_update = QtCore.pyqtSignal(Job)
    queue_update = QtCore.pyqtSignal(list)
    queue_selected = QtCore.pyqtSignal(list)
    job_error = QtCore.pyqtSignal(Job)
    job_error_log = QtCore.pyqtSignal(str)

    def __init__(self, window):
        super().__init__()

        self.state = QueueState.STOPPED

        self.window = window
        self.jobs = []

        self.currentJobState = None

        self.start()
        self.add_actions()

    def add_actions(self):
        self.window.queueStart.clicked.connect(self.start_queue)
        self.window.queueStop.clicked.connect(self.stop)
        self.window.queueClear.clicked.connect(self.clear)
        self.window.queueUp.clicked.connect(self.up)
        self.window.queueDown.clicked.connect(self.down)
        self.window.queueRemove.clicked.connect(self.remove)

    def start_queue(self):
        for job in self.jobs:
            job.state = JobState.QUEUED
        self.state = QueueState.RUNNING
        self.queue_update.emit(self.jobs)

    def stop(self):
        self.state = QueueState.STOPPED
        for job in self.jobs:
            job.state = JobState.STOPPED
        self.queue_update.emit(self.jobs)

    def clear(self):
        self.jobs.clear()
        self.queue_update.emit(self.jobs)

    def up(self):
        indexes = self.window.queue_table.selected_jobs()
        for i, index in enumerate(indexes):
            if index > 0:
                self.jobs.insert(index - 1, self.jobs.pop(index))
                indexes[i] = indexes[i] - 1
        self.queue_update.emit(self.jobs)
        self.queue_selected.emit(indexes)

    def down(self):
        indexes = self.window.queue_table.selected_jobs()
        for i, index in enumerate(indexes):
            if index < len(self.jobs) - 1:
                self.jobs.insert(index + 1, self.jobs.pop(index))
                indexes[i] = indexes[i] + 1
        self.queue_update.emit(self.jobs)
        self.queue_selected.emit(indexes)

    def remove(self):
        indexes = self.window.queue_table.selected_jobs()
        self.jobs = [job for job_i, job in enumerate(self.jobs) if job_i not in indexes]
        self.queue_update.emit(self.jobs)

    def add_jobs(self, details):
        try:
            for params in details:
                self.jobs.append(
                    Job(
                        *params,
                        self.window.encoding,
                        self.window.cache_enabled,
                        self.job_update,
                        self.job_error_log,
                    )
                )
        except Exception as e:
            self.job_error_log.emit(format_exc())

        self.queue_update.emit(self.jobs)

    def test(self):
        print("Hello")

    def run(self):
        while True:
            try:
                if self.state == QueueState.RUNNING:
                    self.inc_job()
                elif self.state == QueueState.STOPPED:
                    sleep(1)
            except Exception as e:
                if len(self.jobs) > 0:
                    job = self.jobs.pop(0)
                    self.job_error.emit(job)
                    job.pickle()

                    hint = _api_error_hint(e)
                    if hint:
                        self.job_error_log.emit(hint)

                    if not isinstance(e, IterError):
                        self.job_error_log.emit(format_exc())
                self.stop()

    def inc_job(self):
        if len(self.jobs) > 0:
            value = self.jobs[0].inc_data()

            if value:
                currentJobState = self.jobs[0].state
                if self.currentJobState != currentJobState:
                    self.currentJobState = currentJobState
                    self.queue_update.emit(self.jobs)
            else:
                self.jobs.pop(0)
                self.currentJobState = None
                self.queue_update.emit(self.jobs)

        else:
            self.state = QueueState.STOPPED
            self.queue_update.emit(self.jobs)

    def stop_retrying(self, _):
        if len(self.jobs) > 0:
            self.jobs[0].source.api.force_stop = True

    def display_value(self, value):
        print(value)
