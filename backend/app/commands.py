import click
from flask import Blueprint
from app.models import UserAccount, Video
import redis
import boto3

from .helpers import db

bp = Blueprint('manage', __name__)

@bp.cli.command('reset_db')
def reset_db():
    v_num = Video.query.delete()
    u_num = UserAccount.query.delete()

    db.engine.execute('ALTER SEQUENCE video_id_seq RESTART WITH 1;')
    db.engine.execute('ALTER SEQUENCE user_account_id_seq RESTART WITH 1;')

    db.session.commit()

    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('video_id_counter', 0)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('youtube-clone-dev-storage')
    bucket.objects.filter(Prefix="video/").delete()

    print('Database reset\nVideos deleted: {}\nChannels deleted: {}'.format(v_num, u_num))

@bp.cli.command('generate_db')
def generate_db():

    

    user_a = UserAccount(username="john")
    user_a.set_password("password")

    user_b = UserAccount(username="adam")
    user_b.set_password("password1")

    db.session.add(user_a)
    db.session.add(user_b)

    db.session.add(
        Video(title="Hello World!", channel_id="2")
    )

    db.session.add(
        Video(title="My life!", channel_id="2")
    )

    db.session.commit()

    print('Generated some dummy data')