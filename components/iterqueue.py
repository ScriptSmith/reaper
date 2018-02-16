from PyQt5 import QtWidgets, QtCore, QtGui
import socialreaper

from .queuewidgets import QueueTable


class Queue(QtCore.QThread):
    job_table = QtCore.pyqtSignal(list)

    progress_bar = QtCore.pyqtSignal(int)
    progress_table = QtCore.pyqtSignal(list)

    job_complete = QtCore.pyqtSignal(str)

    def __init__(self, window):
        super().__init__()

        self.window = window
        window.queueStart.clicked.connect(self.start)
        self.jobs = []

    def add_iterator(self, details):
        try:
            for tup in details:
                sourceName, sourceKeys, functionName, functionArgs, outputPath = tup

                iterator = eval("socialreaper.{}(**{}).{}({})".format(sourceName, sourceKeys, functionName, functionArgs))

                job = {
                    'iterator': iterator,
                    'outputPath': outputPath,
                    'sourceName': sourceName,
                    'sourceFunction': functionName,
                    'functionArgs': functionArgs,
                    'sourceKeys': sourceKeys,
                    'status': 'queued'
                }

                self.jobs.append(job)
        except Exception as e:
            print(f"Error occurred adding iterator\n{e}")

        self.job_table.emit(self.jobs)

    def test(self):
        print("Hello")

    def run(self):
        print("Running")
        for job in self.jobs:
            for datum in job.get('iterator'):
                print(datum)


class IterateData(QtCore.QThread):
    item_generated = QtCore.pyqtSignal(dict)
    progress_changed = QtCore.pyqtSignal(int)
    api_error = QtCore.pyqtSignal(Exception)

    def __init__(self, iterator):
        super().__init__()

        self.iterator = iterator

    def run(self):
        for count, item in enumerate(self.iterator):
            print(item)
