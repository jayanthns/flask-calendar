from common.util.template_decorators import admin_required
from flask_login import login_required
import logging

from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from flask_login import (login_user, logout_user, current_user, login_required)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static'
)


@admin_blueprint.route(
    '/',
    strict_slashes=False
)
@login_required
@admin_required
def dashboard():
    data = {}
    return render_template('admin/dashboard.html', data=data)


@admin_blueprint.route(
    '/user-management',
    strict_slashes=False
)
@login_required
@admin_required
def user_management():
    data = {
        'nbar': 'u_management'
    }
    return render_template('admin/user_management.html', data=data)


@admin_blueprint.route(
    '/user-management/add-user',
    strict_slashes=False,
    methods=['GET', 'POST']
)
@login_required
@admin_required
def add_user():
    data = {
        'nbar': 'u_management'
    }
    return render_template('admin/add_user.html', data=data)


@admin_blueprint.route(
    '/calendar-management',
    strict_slashes=False
)
@login_required
@admin_required
def calendar_management():
    data = {
        'nbar': 'c_management'
    }
    return render_template('admin/calendar_management.html', data=data)
