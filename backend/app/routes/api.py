from flask import Blueprint, render_template, abort, request, jsonify, current_app
from app.models import Video
import subprocess, boto3, redis, os, shutil, time, traceback, tempfile, datetime

from ..helpers import db

bp = Blueprint('api', __name__)

def generate_video_id():
    r = redis.Redis(host='localhost', port=6379, db=0)
    vid_id = r.incr('video_id_counter')
    return vid_id

def video_dir_format(id):
    return "video/{}".format(id)

def get_current_time():
    return datetime.datetime.now()

@bp.route("/upload_video", methods=['POST'])
def upload_video():

    title = request.args.get('title')
    channel_id = request.args.get('channel_id')
    description = request.args.get('description')
    file = request.files['file']

    BUCKET_NAME = current_app.config['BUCKET_NAME']
    BUCKET_URL_PREFIX = current_app.config['BUCKET_URL_PREFIX']

    try:
        s3_client = boto3.client("s3")
        video_id = generate_video_id()

        temp = tempfile.mkstemp()
        os.write(temp[0], file.read())

        """
        try:
            result = subprocess.check_output(["ffmpeg", "-v", "error", "-i", temp[1], "-f", "null", "-", "2"])
        except subprocess.CalledProcessError:
            os.remove(temp[1])
            return {"Message":"Failure: Not a valid video file"}
        """

        tempdir = tempfile.mkdtemp()

        subprocess.run(["ffmpeg", "-i", temp[1], "-f", "dash", os.path.join(tempdir, "out.mpd")])

        for filename in os.listdir(tempdir):
            s3_client.upload_file(os.path.join(tempdir, filename), BUCKET_NAME, "{}/{}".format(video_dir_format(video_id), filename))

        shutil.rmtree(tempdir)
        os.remove(temp[1])

        video = Video(
            channel_id=channel_id,
            upload_date=get_current_time(),
            title=title,
            description=description,
            view_count=0,
            manifest_url="{}/{}/{}".format(BUCKET_URL_PREFIX, video_dir_format(video_id), "out.mpd")
        )

        db.session.add(video)
        db.session.commit()
        
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        pass

    return {"filename": file.filename}

@bp.route("/upload_video_2", methods=['POST'])
def upload_video_2():
    title = request.args.get('title')
    channel_id = request.args.get('channel_id')
    description = request.args.get('description')
    manifest_url = request.args.get('manifest_url')
    thumbnail_url = request.args.get('thumbnail_url')

    BUCKET_NAME = current_app.config['BUCKET_NAME']
    BUCKET_URL_PREFIX = current_app.config['BUCKET_URL_PREFIX']

    try:
        video = Video(
            channel_id=channel_id,
            upload_date=get_current_time(),
            title=title,
            description=description,
            view_count=0,
            manifest_url=manifest_url,
            thumbnail_url=thumbnail_url
        )
        db.session.add(video)
        db.session.commit()
    except Exception:
        pass

    return {"": ""}