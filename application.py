import os

from flask import Flask

from flask_migrate import MigrateCommand
from extensions import (
    bcrypt,
    db,
    migrate,
    ma,
    jwt,
    login_manager,
)
import logging.config
from login_manager_helper import *

# models import
from models.article import *
from models.user import *
from models.calendar import *

# Template View's blueprint
from apps.index.views import index_blueprint
from apps.user_app.views import user_blueprint
from apps.calendar.views import calendar_blueprint

# API View's blueprint
from apps.article.api.views import article_api_blueprint
from apps.user_app.api.views import user_api_blueprint

SETTINGS_FILE = os.environ.get("FLASK_ENV", "settings.dev_settings")


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    # cache.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)
    # redis_store.init_app(app)
    logging.config.dictConfig(app.config["LOGGING"])
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(public.views.blueprint)
    app.register_blueprint(index_blueprint, url_prefix="")
    app.register_blueprint(user_blueprint, url_prefix="/users")
    app.register_blueprint(calendar_blueprint, url_prefix="/calendar")

    app.register_blueprint(article_api_blueprint, url_prefix="/api/articles")
    app.register_blueprint(user_api_blueprint, url_prefix="/api/users")
    return app


def create_app(config_object='settings.base_settings'):
    """Creating the app instance function

    Keyword Arguments:
        config_object {settings} -- [description] (default: {'settings.base_settings'})
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config.from_object(SETTINGS_FILE)
    register_extensions(app)
    register_blueprints(app)
    return app
