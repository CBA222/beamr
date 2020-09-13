from sqlalchemy import create_engine
from flask import current_app
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def get_engine():
    params = {
        "host": "test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com",
        "database": "youtube_sql",
        "user": "postgres",
        "password": "lego_10010"
    }

    from sqlalchemy import create_engine
    engine = create_engine(
        'postgresql://{}:{}@{}/{}'.format(params["user"], params["password"], params["host"], params["database"])
        )

    return engine