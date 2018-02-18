from enum import Enum

from PyQt5 import QtWidgets, QtCore

from ..job_queue import Job, JobState


class ProgressState(Enum):
    PAUSED = "Continue"
    RUNNING = "Pause"


class ProgressWidget(QtWidgets.QWidget):
    def __init__(self, job_signal, tabWidget, parent=None):
        super().__init__(parent=parent)

        self.tabWidget = tabWidget
        job_signal.connect(self.set_job)

        self.state = ProgressState.RUNNING
        self.job = None
        self.show_snapshot = False

        self.MAX_ROWS = 20

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.create_state_widget()
        self.create_snapshot()
        # self.create_dump()
        # self.create_headings()
        # self.create_log()

    def create_state_widget(self):
        stateWidget = QtWidgets.QWidget()
        stateWidget.layout = QtWidgets.QHBoxLayout()
        stateWidget.layout.setContentsMargins(11, 0, 11, 0)
        stateWidget.setLayout(stateWidget.layout)

        self.stateLabel = QtWidgets.QLabel("State: Stopped")
        stateWidget.layout.addWidget(self.stateLabel)

        self.rowCount = QtWidgets.QLabel("Rows: " + str(0))
        stateWidget.layout.addWidget(self.rowCount)

        stateWidget.layout.addStretch(1)

        self.pauseButton = QtWidgets.QPushButton(ProgressState.RUNNING.value)
        self.pauseButton.clicked.connect(self.pause)
        stateWidget.layout.addWidget(self.pauseButton)

        self.layout.addWidget(stateWidget)

    def pause(self, _):
        if self.state == ProgressState.RUNNING:
            self.state = ProgressState.PAUSED
        else:
            self.state = ProgressState.RUNNING

        self.pauseButton.setText(self.state.value)
        self.stateLabel.setText("State: " + str(self.state.value))

    def create_snapshot(self):
        self.snapshotCheckBox = QtWidgets.QCheckBox("Show snapshot")
        self.snapshotCheckBox.toggled.connect(self.toggle_snapshot)
        self.layout.addWidget(self.snapshotCheckBox)

        self.snapshot = QtWidgets.QTableWidget()
        self.snapshot.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.snapshot.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.snapshot.horizontalHeader().setCascadingSectionResizes(True)
        self.layout.addWidget(self.snapshot)

    def update_snapshot(self):
        state = self.job.state
        self.stateLabel.setText("State: " + str(state.value))

        if self.tabWidget.currentIndex() != 4:
            return

        data = list(self.job.flat_data)
        keys = set(self.job.flat_keys)
        # Otherwise it changes during update

        rows = len(data)
        self.rowCount.setText("Rows: " + str(rows))

        # Reduce update rate
        if not (rows % self.MAX_ROWS and state) == JobState.RUNNING or not self.show_snapshot:
            return

        if rows > self.MAX_ROWS:
            self.snapshot.setRowCount(self.MAX_ROWS)
            self.snapshot.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.snapshot.setVerticalHeaderLabels((str(val) for val in range(rows - self.MAX_ROWS + 1, rows + 1)))
        else:
            self.snapshot.setRowCount(rows)

        self.snapshot.setColumnCount(len(keys))
        self.snapshot.setHorizontalHeaderLabels(keys)

        for row_c, datum in enumerate(data[-25:]):
            for col_c, heading in enumerate(keys):
                text = datum.get(heading)
                if text:
                    item = QtWidgets.QTableWidgetItem(text)
                    self.snapshot.setItem(row_c, col_c, item)

    def clear_snapshot(self):
        self.snapshot.setColumnCount(0)
        self.snapshot.setRowCount(0)

    def toggle_snapshot(self, bool):
        self.show_snapshot = bool
        if not bool:
            self.clear_snapshot()

    @QtCore.pyqtSlot(Job)
    def set_job(self, job):
        self.job = job
        self.update_snapshot()
