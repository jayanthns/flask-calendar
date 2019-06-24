import os
import datetime
from environs import Env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    os.environ.get("DB_USERNAME"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_HOST"),
    os.environ.get("DB_PORT"),
    os.environ.get("DB_NAME")
)

env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='settings.dev_settings')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = URI
SECRET_KEY = '(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7'
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)
# DEBUG_TB_ENABLED = DEBUG
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
# WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
# REDIS_URL = "redis://0.0.0.0:6379/0"
# REDIS_URL = env.str('REDIS_URL', None)


# JWT settings
JWT_SECRET_KEY = SECRET_KEY
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
JWT_ACCESS_COOKIE_PATH = "/"
JWT_TOKEN_LOCATION = ['cookies']
JWT_ERROR_MESSAGE_KEY = "message"
JWT_ACCESS_COOKIE_NAME = "x-access-token"
JWT_HEADER_TYPE = "Bearer"
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
