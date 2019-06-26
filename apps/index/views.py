from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from flask_login import login_required, current_user

index_blueprint = Blueprint(
    'index', __name__,
    template_folder='templates',
    # static_folder='static',
    # static_url_path='/static'
)


@index_blueprint.route('/', strict_slashes=False)
@login_required
def index():
    if current_user.is_superuser:
        return redirect(url_for('admin.dashboard'))
    return redirect(url_for('calendar.calendar'))
