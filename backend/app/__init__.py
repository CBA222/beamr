import os
from flask import Flask
from .routes import login, videos, api, comments, search
from . import commands
from flask_migrate import Migrate

from .helpers import db, login_manager

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('BEAMR_SETTINGS')

    app.register_blueprint(login.bp)
    app.register_blueprint(videos.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(comments.bp)
    app.register_blueprint(search.bp)

    app.register_blueprint(commands.bp)

    db.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    return app