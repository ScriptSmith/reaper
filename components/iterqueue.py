from PyQt5 import QtWidgets, QtCore, QtGui
import socialreaper

class Queue(QtCore.QThread):
    def __init__(self, window):
        super().__init__()

        self.window = window
        window.queueStart.clicked.connect(self.run)
        self.iterators = []

    def add_iterator(self, sourceName, sourceKeys, functionName, functionArgs, outputPath):
        try:
            iterator = eval("socialreaper.{}(**{}).{}({})".format(sourceName, sourceKeys, functionName, functionArgs))
            print(iterator)

            itr = {
                'iterator': iterator,
                'outputPath': outputPath,
                'sourceName': sourceName,
                'functionArgs': functionArgs,
                'sourceKeys': sourceKeys
            }

            self.iterators.append(itr)
        except Exception as e:
            print(f"Error occurred adding iterator\n{e}")

    def test(self):
        print("Hello")

    def run(self):
        print("Running")
        for job in self.iterators:
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