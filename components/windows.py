import json
from os import sep
from pathlib import Path
from pprint import pformat
from shutil import rmtree

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

from components.globals import *
from .job_queue import Job
from .widgets.nodes import PathWidget


class PopupWindow(QtWidgets.QMessageBox):

    def __init__(self, title, text, details=None, width=200, height=400):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setDetailedText(details)
        self.setWindowIcon(QtGui.QIcon("ui/icon.png"))
        self.setMinimumWidth(width)
        self.setMinimumWidth(height)

    def pop(self, _):
        print("pop")
        self.exec_()


class ScrollWindow(QtWidgets.QMainWindow):

    def __init__(self, title, subtitle, layout=QtWidgets.QVBoxLayout, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.layout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.mainWidget.setLayout(self.mainWidget.layout)
        self.setCentralWidget(self.mainWidget)

        if subtitle:
            self.mainWidget.layout.addWidget(QtWidgets.QLabel(subtitle))

        self.scrollArea = QtWidgets.QScrollArea(self.mainWidget)
        self.scrollArea.setWidgetResizable(True)

        self.contents = QtWidgets.QWidget(self.scrollArea)
        self.contents.layout = layout()
        self.contents.setLayout(self.contents.layout)
        self.mainWidget.layout.addWidget(self.contents)
        self.mainWidget.layout.addWidget(self.scrollArea)

        self.scrollArea.setWidget(self.contents)


class LicenseWidget(QtWidgets.QWidget):

    def __init__(self, text, details, parent=None):
        super().__init__(parent=parent)
        self.setMinimumHeight(300)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        label = QtWidgets.QLabel(text, self)
        self.layout.addWidget(label)

        browser = QtWidgets.QTextBrowser(self)
        browser.setText(details)
        self.layout.addWidget(browser)


class LicenseWindow(ScrollWindow):

    def __init__(self, bundle_dir, parent=None):
        super().__init__("Software licenses", "Licenses", parent=parent)
        self.setFixedWidth(400)

        self.bundle_dir = bundle_dir

        with open(f"{self.bundle_dir}{sep}LICENSE.txt", "r") as f:
            reaper = LicenseWidget("Reaper GPL license", f.read(), self)
            self.contents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/socialreaper.txt", "r") as f:
            reaper = LicenseWidget("Social Reaper MIT license", f.read(), self)
            self.contents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}LICENSE.txt", "r") as f:
            reaper = LicenseWidget("PyQt GPL license", f.read(), self)
            self.contents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/requests.txt", "r") as f:
            reaper = LicenseWidget("Requests Apache license", f.read(), self)
            self.contents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/requests-oauthlib.txt", "r") as f:
            reaper = LicenseWidget("Requests-OAuthLib ISC license", f.read(), self)
            self.contents.layout.addWidget(reaper)

        with open(f"{self.bundle_dir}{sep}licenses/oauthlib.txt", "r") as f:
            reaper = LicenseWidget("OAuthLib BSD license", f.read(), self)
            self.contents.layout.addWidget(reaper)

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
        self.setMinimumSize(500, 500)

        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.layout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.mainWidget.setLayout(self.mainWidget.layout)
        self.setCentralWidget(self.mainWidget)

        self.tabs = QtWidgets.QTabWidget(self.mainWidget)

        self.console = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.console, "Error log")

        self.job_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.job_browser, "Job state")

        self.itr_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.itr_browser, "Iterator state")

        self.api_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.api_browser, "API state")

        self.error_browser = QtWidgets.QTextBrowser()
        self.tabs.addTab(self.error_browser, "Error state")

        self.toggle_job_tabs(False)

        self.mainWidget.layout.addWidget(self.tabs)

        self.cancelButton = QtWidgets.QPushButton("Stop retrying", self.mainWidget)
        self.mainWidget.layout.addWidget(self.cancelButton)

        self.options = self.menuBar().addMenu("Options")
        self.clearAction = QtWidgets.QAction("Clear")
        self.clearAction.triggered.connect(self.clear)
        self.options.addAction(self.clearAction)

    def toggle_job_tabs(self, boolean):
        for i in range(1, 5):
            self.tabs.setTabEnabled(i, boolean)

    def clear(self, _):
        self.log = ""
        self.toggle_job_tabs(False)
        self.console.clear()
        self.job_browser.clear()
        self.itr_browser.clear()
        self.api_browser.clear()
        self.error_browser.clear()

    @QtCore.pyqtSlot(Job)
    def throw_job(self, job):
        self.toggle_job_tabs(True)
        self.job_browser.setText(pformat(vars(job)))
        self.itr_browser.setText(str(job.iterator))
        self.api_browser.setText(str(job.source.api))
        self.error_browser.setText(str(job.error))
        self.show()

    def log_error(self, log):
        self.show()
        self.log += log + "\n"
        self.console.setText(self.log)
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())


class BinaryBox(QtWidgets.QGroupBox):

    def __init__(
        self, title, choices, description, default_choice, toggle_function, parent=None
    ):
        super().__init__(parent)
        self.toggle_function = toggle_function

        self.setTitle(title)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.layout.addWidget(QtWidgets.QLabel(description, self))

        self.option_1 = QtWidgets.QRadioButton(choices[0], self)
        self.layout.addWidget(self.option_1)

        self.option_2 = QtWidgets.QRadioButton(choices[1], self)
        self.layout.addWidget(self.option_2)

        self.option_1.toggled.connect(toggle_function)
        self.option_2.toggled.connect(self.invert)

        if default_choice:
            self.option_1.toggle()
        else:
            self.option_2.toggle()

    def invert(self, boolean):
        self.toggle_function(not boolean)


class SettingsWindow(ScrollWindow):

    def __init__(self, parent):
        super().__init__(
            "Settings", None, layout=QtWidgets.QFormLayout, parent=parent.window
        )
        self.setMinimumSize(400, 475)
        self.location = f"{DATA_DIR}{sep}settings.json"
        self.parent = parent

        self.data = {
            "save_path": f"{Path.home()}{sep}Downloads",
            "light": True,
            "utf-8": True,
            "cache": True,
        }
        self.load_settings()

        self.savePathBox = QtWidgets.QGroupBox(self)
        self.savePathBox.setTitle("Output directory")
        self.savePathBox.layout = QtWidgets.QVBoxLayout()
        self.savePathBox.setLayout(self.savePathBox.layout)

        self.savePath = PathWidget(self.data.get("save_path"))
        self.savePath.path_changed.connect(self.set_save_path)
        self.savePathBox.layout.addWidget(self.savePath)

        self.contents.layout.addWidget(self.savePathBox)

        self.themeBox = BinaryBox(
            "Theme",
            ("Light", "Dark"),
            "Change Reaper's Appearance",
            self.get_light_mode(),
            self.set_light_mode,
        )
        self.contents.layout.addWidget(self.themeBox)

        self.encodingBox = BinaryBox(
            "Output encoding",
            ("UTF-8", "ASCII"),
            "Changing to ASCII will mean non-ASCII data will be lost",
            self.get_encoding(),
            self.set_encoding,
        )
        self.contents.layout.addWidget(self.encodingBox)

        self.cacheBox = BinaryBox(
            "Cache",
            ("Use cache and memory", "Use memory"),
            "Store large data on disk",
            self.get_cache_mode(),
            self.set_cache,
        )

        clearCacheButton = QtWidgets.QPushButton("Clear cache")
        clearCacheButton.clicked.connect(self.clear_cache)
        clearCacheButtonLayout = QtWidgets.QWidget()
        clearCacheButtonLayout.layout = QtWidgets.QHBoxLayout(clearCacheButtonLayout)
        clearCacheButtonLayout.layout.setContentsMargins(0, 0, 0, 0)
        clearCacheButtonLayout.setLayout(clearCacheButtonLayout.layout)
        clearCacheButtonLayout.layout.addWidget(clearCacheButton)
        clearCacheButtonLayout.layout.addStretch(1)

        self.cacheBox.layout.addWidget(clearCacheButtonLayout)
        self.contents.layout.addWidget(self.cacheBox)

        self.saveButtonWidget = QtWidgets.QWidget(self.contents)
        self.saveButtonWidget.layout = QtWidgets.QHBoxLayout(self.saveButtonWidget)
        self.saveButtonWidget.setLayout(self.saveButtonWidget.layout)
        self.contents.layout.addWidget(self.saveButtonWidget)

        self.saveButton = QtWidgets.QPushButton("Save", self.saveButtonWidget)
        self.saveButton.clicked.connect(self.save)
        self.saveButtonWidget.layout.addWidget(self.saveButton)
        self.saveButtonWidget.layout.addStretch(1)

    def set_light_mode(self, boolean):
        self.parent.enable_dark_mode(boolean)
        self.data["light"] = boolean

    def set_encoding(self, boolean):
        if boolean:
            self.parent.encoding = "utf-8"
        else:
            self.parent.encoding = "ascii"
        self.data["utf-8"] = boolean

    def set_cache(self, boolean):
        self.parent.cache_enabled = boolean
        self.data["cache"] = boolean

    def set_save_path(self, text):
        self.data["save_path"] = text

    def clear_cache(self, boolean):
        rmtree(CACHE_DIR, ignore_errors=True)

    def save(self, _):
        self.hide()
        self.save_settings()

    def save_settings(self):
        with open(self.location, "w") as f:
            json.dump(self.data, f)

    def load_settings(self):
        try:
            with open(self.location, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def get_save_path(self):
        return self.data.get("save_path")

    def get_encoding(self):
        return self.data.get("utf-8")

    def get_light_mode(self):
        return self.data.get("light")

    def get_cache_mode(self):
        return self.data.get("cache")
