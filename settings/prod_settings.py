import os
from settings.base_settings import *
# from settings.log_setting_new import LOGGING
from settings.log_settings import get_log_settings


DEBUG = False
LOG_ROOT = os.path.abspath(os.path.join(BASE_DIR, "logger"))


LOGGING = get_log_settings(
    LOG_ROOT=LOG_ROOT, setting='development', size=5, backup_count=2)
# LOGGING = LOGGING

JWT_COOKIE_SECURE = True
