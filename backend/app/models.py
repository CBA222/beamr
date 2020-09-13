from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .helpers import db, login_manager

class UserAccount(UserMixin, db.Model):
    # ...
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    channel_url = db.Column(db.String(128))
    channel_icon_url = db.Column(db.String(128))
    name = db.Column(db.String(128))
    subscriber_count = db.Column(db.Integer)

    def __repr__(self):
        return '<UserAccount {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.ForeignKey('user_account.id'))
    view_count = db.Column(db.Integer)
    upload_date = db.Column(db.DateTime, index=True)
    title = db.Column(db.String(256))
    description = db.Column(db.String(5000))
    manifest_url = db.Column(db.String(128))
    thumbnail_url = db.Column(db.String(128))
    duration = db.Column(db.Integer) # in seconds

class SubscriberRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    following_id = db.Column(db.Integer)

@login_manager.user_loader
def load_user(id):
    return UserAccount.query.get(int(id))
