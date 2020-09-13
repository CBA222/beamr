from fastapi import APIRouter, HTTPException, FastAPI, File, UploadFile, Query
import time
import subprocess
import tempfile
import os
import boto3
import uuid
import shutil
from sqlalchemy import text, create_engine, MetaData, Table
import datetime
from typing import Optional
import redis
import traceback

BUCKET_URL_PREFIX="https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com"
BUCKET_NAME = "youtube-clone-dev-storage"

def generate_video_id():
    r = redis.Redis(host='localhost', port=6379, db=0)
    vid_id = r.incr('video_id_counter')
    return vid_id

def video_dir_format(id):
    return "video/{}".format(id)

def get_engine():
    params = {
        "host": "test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com",
        "database": "youtube_sql",
        "user": "postgres",
        "password": "lego_10010"
    }
    engine = create_engine(
        'postgresql://{}:{}@{}/{}'.format(params["user"], params["password"], params["host"], params["database"])
        )
    return engine

def get_sql_connection():
    engine = get_engine()
    conn = engine.connect()
    return conn

def get_current_time():
    return datetime.datetime.now()

def get_video_table():
    metadata = MetaData()
    engine = get_engine()
    videos = Table('video', metadata, autoload=True, autoload_with=engine)
    return videos

router = APIRouter()

@router.post("/upload_video")
async def upload_video(
    title: str = Query(None, max_length=100),
    channel_id: int = Query(None),
    description: str = Query("", max_length=1000),
    file: UploadFile = File(...),
    thumbnail_file: Optional[UploadFile] = None
):
    try:
        s3_client = boto3.client("s3")
        video_id = generate_video_id()

        temp = tempfile.mkstemp()
        os.write(temp[0], file.file.read())

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

        videos = get_video_table()
        ins = videos.insert().values(
            channel_id=channel_id,
            upload_date=get_current_time(),
            title=title,
            description=description,
            view_count=0,
            manifest_url="{}/{}/{}".format(BUCKET_URL_PREFIX, video_dir_format(video_id), "out.mpd")
        )

        # update database
        conn = get_sql_connection()
        conn.execute(ins)
        conn.close()
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        pass

    return {"filename": file.filename}