from os import sep
from pprint import pformat

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

from .job_queue import Job


class PopupWindow(QtWidgets.QMessageBox):
    def __init__(self, title, text, details=None, width=200, height=400):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setDetailedText(details)
        self.setWindowIcon(QtGui.QIcon('ui/icon.png'))
        self.setMinimumWidth(width)
        self.setMinimumWidth(height)

    def pop(self, _):
        print("pop")
        self.exec_()


class LicenseWidget(QtWidgets.QWidget):
    def __init__(self, text, details, parent=None):
        super().__init__(parent=parent)
        self.setMinimumHeight(300)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        label = QtWidgets.QLabel(text)
        self.layout.addWidget(label)

        browser = QtWidgets.QTextBrowser()
        browser.setText(details)
        self.layout.addWidget(browser)


class LicenseWindow(QtWidgets.QMainWindow):
    def __init__(self, bundle_dir, parent=None):
        super().__init__(parent=parent)
        self.bundle_dir = bundle_dir

        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.layout = QtWidgets.QVBoxLayout()
        self.mainWidget.setLayout(self.mainWidget.layout)
        self.setCentralWidget(self.mainWidget)

        self.setFixedWidth(450)
        self.setWindowTitle("Software Licenses")
        self.setWindowIcon(QtGui.QIcon('ui/icon.ico'))

        self.mainWidget.layout.addWidget(QtWidgets.QLabel("Licenses"))

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.layout = QtWidgets.QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.scrollAreaWidgetContents.layout)
        self.mainWidget.layout.addWidget(self.scrollAreaWidgetContents)
        self.mainWidget.layout.addWidget(self.scrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        with open(f"{self.bundle_dir}{sep}LICENSE.txt", 'r') as f:
            reaper = LicenseWidget("Reaper GPL license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/socialreaper.txt", 'r') as f:
            reaper = LicenseWidget("Social Reaper MIT license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}LICENSE.txt", 'r') as f:
            reaper = LicenseWidget("PyQt GPL license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/requests.txt", 'r') as f:
            reaper = LicenseWidget("Requests Apache license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/requests-oauthlib.txt", 'r') as f:
            reaper = LicenseWidget("Requests-OAuthLib ISC license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/oauthlib.txt", 'r') as f:
            reaper = LicenseWidget("OAuthLib BSD license", f.read())
            self.scrollAreaWidgetContents.layout.addWidget(reaper)

    def pop(self):
        self.show()


class ErrorWindow(QtWidgets.QMainWindow):
    job_error = pyqtSignal(Job)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.job_error.connect(self.throw_job)
        self.job = None
        self.log = ""

        self.setWindowTitle("Error manager")
        self.setMinimumSize(400, 400)

        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.layout = QtWidgets.QVBoxLayout()
        self.mainWidget.setLayout(self.mainWidget.layout)
        self.setCentralWidget(self.mainWidget)

        self.tabs = QtWidgets.QTabWidget()

        self.console = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.console, "Error log")

        self.job_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.job_browser, "Job state")

        self.itr_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.itr_browser, "Iterator state")

        self.api_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.api_browser, "API state")

        self.toggle_job_tabs(False)

        self.mainWidget.layout.addWidget(self.tabs)

        self.options = self.menuBar().addMenu("Options")
        self.clearAction = QtWidgets.QAction("Clear")
        self.clearAction.triggered.connect(self.clear)
        self.options.addAction(self.clearAction)

    def toggle_job_tabs(self, boolean):
        for i in range(1,4):
            self.tabs.setTabEnabled(i, boolean)

    def clear(self, _):
        self.log = ""
        self.toggle_job_tabs(False)
        self.console.clear()
        self.job_browser.clear()
        self.itr_browser.clear()
        self.api_browser.clear()

    @QtCore.pyqtSlot(Job)
    def throw_job(self, job):
        self.toggle_job_tabs(True)
        self.job_browser.setText(pformat(vars(job)))
        self.itr_browser.setText(str(job.iterator))
        self.api_browser.setText(str(job.source.api))
        self.show()

    def log_error(self, log):
        self.show()
        self.log += log + '\n'
        self.console.setText(self.log)
