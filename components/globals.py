import appdirs
import sys
import os

APP_NAME = "Reaper"
APP_AUTHOR = "UQ"

DATA_DIR = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)
LOG_DIR = appdirs.user_log_dir(APP_NAME, APP_AUTHOR)
CACHE_DIR = appdirs.user_cache_dir(APP_NAME, APP_AUTHOR)

def _calc_path(path):
    head, tail = os.path.split(path)
    if tail == 'reaper':
        return path
    else:
        return _calc_path(head)

BUNDLE_DIR = sys._MEIPASS if getattr(sys, "frozen", False) else \
    _calc_path(os.path.dirname(os.path.abspath(__file__)))
