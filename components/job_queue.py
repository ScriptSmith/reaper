from enum import Enum
from os import path, makedirs
from pickle import dump
from time import sleep
from traceback import format_exc

from PyQt5 import QtCore
from appdirs import user_log_dir

import socialreaper
from socialreaper.iterators import IterError


class QueueState(Enum):
    RUNNING = "running"
    STOPPED = "stopped"


class JobState(Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    QUEUED = "queued"
    SAVING = "saving"
    FINISHED = "finished"


class Job():
    error_log = QtCore.pyqtSignal(str)

    def __init__(self, outputPath, sourceName, sourceFunction, functionArgs, sourceKeys, append, keyColumn, encoding,
                 job_update, job_error_log):
        self.source = eval(f"socialreaper.{sourceName}(**{sourceKeys})")
        self.source.api.log_function = self.log
        self.log_function = job_error_log
        self.error = None
        self.encoding = encoding

        self.iterator = eval(f"self.source.{sourceFunction}({functionArgs})")
        self.outputPath = outputPath
        self.sourceName = sourceName
        self.sourceFunction = sourceFunction
        self.functionArgs = functionArgs
        self.sourceKeys = sourceKeys

        self.append = append
        self.keyColumn = keyColumn

        self.state = JobState.STOPPED
        self.job_update = job_update
        self.log_data = ""
        self.data = []
        self.flat_data = []
        self.keys = set()
        self.flat_keys = set()

    def log(self, string):
        self.log_function.emit(str(string))

    def add_data(self, data):
        self.data.append(data)
        flat_data = socialreaper.tools.flatten(data)
        self.flat_data.append(flat_data)

        keys = data.keys()
        if keys != self.keys:
            self.keys.update(keys)

        flat_keys = flat_data.keys()
        if flat_keys != self.flat_keys:
            self.flat_keys.update(flat_keys)

    def inc_data(self):
        self.state = JobState.RUNNING
        try:
            value = self.iterator.__next__()
            self.add_data(value)
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
        # except socialreaper.IterError as e:
        #     print("Job Failed")
        #     print(e)
        #     return self.end_job()

    def end_job(self):
        # Save CSV
        self.state = JobState.SAVING
        self.job_update.emit(self)
        socialreaper.tools.CSV(self.flat_data, file_name=self.outputPath, flat=False, append=self.append,
                               key_column=self.keyColumn, encoding=self.encoding)
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

        dir = user_log_dir()

        if not path.exists(dir):
            makedirs(dir)

        with open(f"{dir}/out.pickle", 'wb') as f:
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
                self.jobs.append(Job(*params, self.window.encoding, self.job_update, self.job_error_log))
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
                self.queue_update.emit(self.jobs)


        else:
            self.state = QueueState.STOPPED
            self.queue_update.emit(self.jobs)

    def stop_retrying(self, _):
        if len(self.jobs) > 0:
            self.jobs[0].source.api.force_stop = True

    def display_value(self, value):
        print(value)
