import logging
from functools import wraps

from flask import request, redirect, url_for

from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, decode_token


from models.user import User

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def is_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            user_data = get_jwt_identity()
            user_obj = User.query.filter_by(email=user_data['email']).one()
            setattr(request, 'user', user_obj)
            setattr(request, 'auth_token', request.cookies['x-access-token'])
            token_extra_details = decode_token(request.cookies['x-access-token'])
            token_data = {
                'iat': token_extra_details['iat'],
                'exp': token_extra_details['exp'],
                'identity': token_extra_details['identity'],
                'token': request.cookies['x-access-token']
            }
            setattr(request, 'token_data', token_data)
            return fn(*args, **kwargs)
        except Exception as e:
            return redirect(url_for('user.login'))
    return wrapper
