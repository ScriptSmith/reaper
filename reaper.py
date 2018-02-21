#!/usr/bin/env python3

# Copyright (C) 2017 Adam Smith

# This file is part of Reaper

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from components.job_queue import Queue
from components.keys import KeyPage
from components.sources import SourceTabs
from components.widgets.nodes import PrimaryInputWindow
from components.widgets.progress import ProgressWidget
from components.widgets.queue import QueueTable
from mainwindow import Ui_MainWindow


class Reaper(Ui_MainWindow):
    def __init__(self, window, app, show=True):
        super().__init__()

        self.version = "v2.0"
        self.source_file = 'sources.xml'

        self.window = window

        self.app = app

        if show:
            window.show()

        self.setupUi(window)

        self.window.setWindowIcon(QIcon('ui/icon.png'))
        self.window.setWindowTitle(f"Reaper {self.version}")

        self.advanced_mode = False
        self.dark_mode = False

        self.add_actions()

        # Create queue page
        self.queue = Queue(self)
        self.set_icons()

        # Create queue table
        self.queue_table = QueueTable()
        self.queueLayout.addWidget(self.queue_table)

        # Create window for primary key input
        self.primaryInputWindow = PrimaryInputWindow(window)

        # Create api key page
        self.key_page = KeyPage(self.scrollAreaWidgetContents)

        # Create sources page
        self.source_tabs = SourceTabs(self, self.key_page, self.source_file, self.primaryInputWindow)

        # Create progress page
        self.progress_page = ProgressWidget(self.queue.job_update, self.tabWidget)
        self.progressLayout.addWidget(self.progress_page)

    def enable_advanced_mode(self, bool):
        self.advanced_mode = bool

    def enable_dark_mode(self, bool):
        if bool:
            self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            self.app.setStyleSheet("")

    def add_actions(self):
        self.actionAdvanced_mode.toggled.connect(self.enable_advanced_mode)
        self.actionDark_mode.toggled.connect(self.enable_dark_mode)
        self.actionQuit.triggered.connect(self.quit)

    def set_icons(self):
        self.queueUp.setIcon(QIcon('ui/up.png'))
        self.queueDown.setIcon(QIcon('ui/down.png'))
        self.queueRemove.setIcon(QIcon('ui/remove.png'))
        self.window.setWindowIcon(QIcon('ui/icon.ico'))

    def quit(self, _):
        self.app.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Reaper(main_window, app)
    sys.exit(app.exec_())
