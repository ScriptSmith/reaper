import appdirs
import sys
import os

APP_NAME = "Reaper"
APP_AUTHOR = "UQ"

DATA_DIR = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)
LOG_DIR = appdirs.user_log_dir(APP_NAME, APP_AUTHOR)
CACHE_DIR = appdirs.user_cache_dir(APP_NAME, APP_AUTHOR)


def _calc_path(path):
    """
    Resolve the project root directory without recursive parent traversal.

    The original implementation recursively walked parent directories until it
    found a folder named "reaper". On Windows this can loop forever when the
    path reaches a drive boundary (e.g. "D:\\") and os.path.split() keeps
    returning the same head.
    """
    current = os.path.abspath(path)
    start = current

    while True:
        if (
            os.path.isdir(os.path.join(current, "ui"))
            and os.path.isdir(os.path.join(current, "components"))
        ):
            return current

        head, _ = os.path.split(current)
        if head == current or head == "":
            return start

        current = head

BUNDLE_DIR = sys._MEIPASS if getattr(sys, "frozen", False) else \
    _calc_path(os.path.dirname(os.path.abspath(__file__)))
