from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def easy_date_format(difference):

    if difference.seconds < 60 * 60 * 24:

        return '{:.0f} hours ago'.format(difference.seconds / (60 *24))

        if difference.seconds < 60 * 60:

            return '{:.0f} minutes ago'.format(difference.seconds / 60)

            if difference.seconds < 60:

                return '{:.0f} seconds ago'.format(difference.seconds)

    return '{:.0f} days ago'.format(difference.days)

