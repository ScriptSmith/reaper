import sys
from unittest import TestCase

from PyQt5 import QtWidgets

import reaper
app = QtWidgets.QApplication(sys.argv)


class TestReaper(TestCase):
    def setUp(self):
        main_window = QtWidgets.QMainWindow()
        self.reaper = reaper.Reaper(main_window, show=True)

    def test_stack_jump(self):
        print("hello")
        self.reaper.stack_jump(3)
        self.assertIs(self.reaper.stackedWidget.currentIndex(), 3)

    def test_stack_auth(self):
        self.fail()

    def test_stack_input(self):
        self.fail()

    def test_stack_progress(self):
        self.fail()

    def test_stack_preferences(self):
        self.fail()

    def test_stack_updates(self):
        self.fail()

    def test_stack_licences(self):
        self.fail()

    def test_exit_generator(self):
        self.fail()

    def test_new_input(self):
        self.fail()

    def test_load_auth_keys(self):
        self.fail()

    def test_save_auth_keys(self):
        self.fail()

    def test_error_message(self):
        self.fail()

    def test_project_url(self):
        self.fail()

    def test_write_console(self):
        self.fail()

    def test_set_status(self):
        self.fail()

    def test_pause_thread(self):
        self.fail()

    def test_fill_table(self):
        self.fail()

    def test_initiate_download(self):
        self.fail()

    def test_save(self):
        self.fail()

    def test_save_csv(self):
        self.fail()

    def test_save_json(self):
        self.fail()

    def test_add_actions(self):
        self.fail()

    def test_connect_library(self):
        self.fail()
