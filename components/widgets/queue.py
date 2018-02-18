from PyQt5 import QtWidgets, QtCore, QtGui

import json

class QueueTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSelectionBehavior(self.SelectRows)
        self.setEnabled(False)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.setColumnCount(6)
        self.setRowCount(1)
        self.setHorizontalHeaderLabels(['Source', 'Function', 'Parameters', 'API Keys', 'Path', 'Status'])
        # self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    @QtCore.pyqtSlot(list)
    def display_jobs(self, jobs):
        if len(jobs) > 0:
            self.setEnabled(True)
        else:
            self.setEnabled(False)
        self.setRowCount(len(jobs))
        for row, job in enumerate(jobs):
            sourceName = QtWidgets.QTableWidgetItem(job.sourceName)
            sourceFunction = QtWidgets.QTableWidgetItem(job.sourceFunction)
            functionArgs = QtWidgets.QTableWidgetItem(job.functionArgs)
            sourceKeys = QtWidgets.QTableWidgetItem(json.dumps(job.sourceKeys))
            outputPath = QtWidgets.QTableWidgetItem(job.outputPath)
            status = QtWidgets.QTableWidgetItem(job.state.value)

            self.setItem(row, 0, sourceName)
            self.setItem(row, 1, sourceFunction)
            self.setItem(row, 2, functionArgs)
            self.setItem(row, 3, sourceKeys)
            self.setItem(row, 4, outputPath)
            self.setItem(row, 5, status)

    def pause_jobs(self):
        pass

    def play_jobs(self):
        pass

    def delete_job(self):
        pass

    def clear_jobs(self):
        pass

        # self.selectRow(0)