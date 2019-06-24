from extensions import login_manager

from models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(email=user_id).one_or_none()


login_manager.login_view = "user.login"
login_manager.login_message = u"User is not logged in."
login_manager.login_message_category = "info"
