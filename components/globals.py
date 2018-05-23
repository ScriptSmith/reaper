import appdirs

APP_NAME = "Reaper"
APP_AUTHOR = "UQ"

DATA_DIR = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)
LOG_DIR = appdirs.user_log_dir(APP_NAME, APP_AUTHOR)
CACHE_DIR = appdirs.user_cache_dir(APP_NAME, APP_AUTHOR)