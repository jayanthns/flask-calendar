import logging

from extensions import jwt
from common.util.common_response import response

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# A storage engine to save revoked tokens.
blacklist = set()

# Using the expired_token_loader decorator, we will now call
# this function whenever an expired but otherwise valid access
# token attempts to access an endpoint


@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    return response(
        message="Token has expired.",
        status=401
    )


@jwt.invalid_token_loader
def my_invalid_token_callback(invalid_token):
    return response(
        message="Invalid token.",
        status=401
    )


@jwt.unauthorized_loader
def my_unauthorized_callback(reason):
    return response(
        message="Unauthorized request",
        status=401
    )


# For this example, we are just checking if the tokens jti
# (unique identifier) is in the blacklist set. This could
# be made more complex, for example storing all tokens
# into the blacklist with a revoked status when created,
# and returning the revoked status in this call. This
# would allow you to have a list of all created tokens,
# and to consider tokens that aren't in the blacklist
# (aka tokens you didn't create) as revoked. These are
# just two options, and this can be tailored to whatever
# your application needs.
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@jwt.revoked_token_loader
def token_in_blacklist_callback(message):
    return response(
        message=message,
        status=401
    )
