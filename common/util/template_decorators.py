import logging
from functools import wraps

from flask import request, redirect, url_for
from flask_login import current_user

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.is_superuser:
            return fn(*args, **kwargs)
        return redirect(url_for('index.index'))
    return wrapper
