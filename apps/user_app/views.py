import logging

from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from flask_login import (login_user, logout_user, current_user, login_required)

from .backends import authenticate
from .forms import LoginForm, ForgotPasswordForm
from common.util.flash_message import set_flash_message

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

user_blueprint = Blueprint(
    'user', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static'
)


@user_blueprint.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    if current_user and not current_user.is_anonymous:
        return redirect(url_for('index.index'))
    form = LoginForm(request.form)
    data = {
        'nbar': 'login'
    }
    if request.method == 'GET':
        return render_template("user/login.html", form=form, data=data)

    if not form.validate():
        set_flash_message("Invalid credentials", "alert-danger")
        return render_template("user/login.html", form=form, data=data)
    user = authenticate(**form.data)
    if not user:
        set_flash_message("Invalid credentials", "alert-danger")
        return render_template("user/login.html", form=form, data=data)
    user.authenticated = True
    user.save()
    login_user(user, remember=True)
    next = request.args.get('next')

    return redirect(next or url_for('index.index'))


@user_blueprint.route('/logout', strict_slashes=False, methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    user.save()
    logout_user()
    return redirect(url_for('user.login'))


@user_blueprint.route('/contact-us', strict_slashes=False)
def contact_us():
    return render_template("user/contact_us.html")


@user_blueprint.route(
    '/forgot-password',
    strict_slashes=False,
    methods=['GET', 'POST']
)
def forgot_password():
    if current_user and not current_user.is_anonymous:
        return redirect(url_for('index.index'))
    form = ForgotPasswordForm(request.form)

    if request.method == 'GET':
        return render_template("user/forgot_password.html", form=form, data={})

    if not form.validate():
        set_flash_message("Incorrect data.", "alert-danger")
        return render_template("user/forgot_password.html", form=form, data={})

    # TODO Password reset email and template
    set_flash_message("Reset password link has sent your mail.")
    return redirect(url_for('user.login'))


@user_blueprint.route(
    '/profile',
    strict_slashes=False,
    methods=['GET', 'POST']
)
@login_required
def profile():
    return render_template("user/profile.html", data={'nbar': 'profile'})
