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

import pickle
import sys
import logging
import tempfile
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSizePolicy, QStyleFactory
from PyQt5.QtCore import QThread, pyqtSignal, QUrl, Qt
from PyQt5.QtGui import QDesktopServices, QTextCursor, QIcon

import qdarkstyle

from mainwindow import Ui_MainWindow
from components.facebook import post as Facebook_Post

from build_sources import build

from socialreaper import Facebook


class Reaper(Ui_MainWindow):
    def __init__(self, window, show=True):
        super().__init__()

        self.version = "v2.0"

        self.window = window
        self.window.setWindowIcon(QIcon('ui/icon.png'))

        if show:
            window.show()

        self.setupUi(window)

        # self.wdg = QtWidgets.QWidget()
        # post = Facebook_Post.Ui_Form()
        # post.setupUi(self.wdg)
        # self.wdg.show()

        self.add_actions()

        build(self)


    def fb_stack_jump(self, i):
        self.fb_stack.setCurrentIndex(i)

    def fb_next_stack(self):
        self.fb_stack_jump(1)

    def add_actions(self):
        # self.fb_next.clicked.connect(self.fb_next_stack)
        pass

    def crap(self):
        self.pageTab.setLayout(QtWidgets.QVBoxLayout())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window = QtWidgets.QMainWindow()
    ui = Reaper(main_window)
    sys.exit(app.exec_())
