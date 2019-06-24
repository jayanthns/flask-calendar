import logging

from flask import Blueprint, request
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity, set_access_cookies,
    unset_jwt_cookies, get_raw_jwt
)

from models.user import User

from common.util.common_response import response
from common.util.decorators import token_required, is_authenticated
from common.util.jwt_token_helpers import blacklist

from apps.user_app.api.serializers import (
    user_schema,
    users_schema,
    user_login_schema
)
from apps.user_app.backends import authenticate

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


user_api_blueprint = Blueprint(
    'user_api', __name__
)


@user_api_blueprint.route("/", methods=['GET', 'POST'], strict_slashes=False)
def users():
    """view for get users"""
    if request.method == "GET":
        users = users_schema.dump(User.query.all())
        return response(
            message="Data fetched successfully.",
            data=users.data,
            status=200
        )

    """View for Creating the user."""
    if request.method == 'POST':
        user_data = user_schema.load(request.get_json() or {})

        if user_data.errors:
            return response(
                message="Incorrect data were provided.",
                data={**user_data.errors},
                status=400
            )

        user = user_data.data
        user.save()
        user = user_schema.dump(user)
        return response(
            message="User created successfully.",
            data=user.data,
            status=201
        )


@user_api_blueprint.route("details/", methods=['GET'], strict_slashes=False)
@token_required
@is_authenticated
def user_details():
    """get user details"""
    serializer = user_schema.dump(request.user)

    return response(
        data=serializer.data,
        message="Data fetched successfully.",
        status=200
    )


@user_api_blueprint.route("login/", methods=['POST'], strict_slashes=False)
def login():
    """View for login user"""
    login_data = user_login_schema.load(request.get_json() or {})

    if login_data.errors:
        return response(
            message="Incorrect data were provided",
            data={**login_data.errors},
            status=400
        )
    user = authenticate(**login_data.data)
    if not user:
        return response(
            message="Invalid credentials.",
            status=400
        )

    user_data = user_schema.dump(user).data
    payload = {
        'email': user.email,
        'id': user.id
    }
    access_token = create_access_token(identity=payload)

    res, status_code = response(
        data=user_data,
        message="User logged in successfully.",
        status=200
    )
    set_access_cookies(res, access_token)
    return res, status_code


@user_api_blueprint.route("logout/", methods=['GET'], strict_slashes=False)
@token_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    res, status_code = response(
        message="Logged out successfully.",
        status=200
    )
    unset_jwt_cookies(res)
    return res, status_code
