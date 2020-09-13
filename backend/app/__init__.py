import os
from flask import Flask
from .routes import login, videos, api
from . import commands
from flask_migrate import Migrate

from .helpers import db, login_manager

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="postgresql://postgres:lego_10010@test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com:5432/youtube_sql",
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        BUCKET_URL_PREFIX="https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com",
        BUCKET_NAME = "youtube-clone-dev-storage"
    )

    app.register_blueprint(login.bp)
    app.register_blueprint(videos.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(commands.bp)

    db.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    return app