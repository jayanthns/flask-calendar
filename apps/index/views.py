from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from flask_login import login_required

from common.util.template_decorators import is_logged_in

index_blueprint = Blueprint(
    'index', __name__,
    template_folder='templates',
    # static_folder='static',
    # static_url_path='/static'
)


@index_blueprint.route('/', strict_slashes=False)
@login_required
def index():
    return redirect(url_for('calendar.calendar'))
