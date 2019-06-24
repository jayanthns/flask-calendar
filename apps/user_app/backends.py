from models.user import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).one_or_none()
    if not user or not user.check_password(password):
        return None
    return user
