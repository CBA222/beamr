from fastapi import FastAPI, File, UploadFile, Query
import subprocess
import tempfile
import os
import boto3
import uuid
import shutil
from sqlalchemy import text, create_engine
import datetime
from typing import Optional
import redis


BUCKET_NAME = "youtube-clone-dev-storage"

app = FastAPI()

def generate_video_id():
    r = redis.Redis(host='localhost', port=6379, db=0)
    vid_id = r.incr('video_id_counter')
    return vid_id

def video_dir_format(id):
    return "video_{}".format(id)

def get_sql_connection():
    params = {
        "host": "test-database.ctyo46w3wzci.us-east-2.rds.amazonaws.com",
        "database": "youtube_sql",
        "user": "postgres",
        "password": "lego_10010"
    }
    engine = create_engine(
        'postgresql://{}:{}@{}/{}'.format(params["user"], params["password"], params["host"], params["database"])
        )
    conn = engine.connect()
    return conn

def get_current_time():
    return datetime.datetime.now()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload_video")
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

        ins = text(
            """
            INSERT INTO videos (video_id, title, channel_id, upload_date, description, manifest_url, thumbnail_url)
            VALUES (:p1, :p2, :p3, :p4, :p5, :p6, :p7);
            """
        )
        ins = ins.bindparams(
            p1=video_id, 
            p2=title, 
            p3=channel_id, 
            p4=get_current_time(), 
            p5=description, 
            p6="{}/{}".format(video_dir_format(video_id), "out.mpd"), 
            p7=None
            )

        # update database
        conn = get_sql_connection()
        conn.execute(ins)
        conn.close()
    except Exception:
        pass
    finally:
        pass

    return {"filename": file.filename}

@app.post("/delete_video")
async def delete_video(video_id: int):
    s3_client = boto3.client("s3")
    objects = s3_client.list_objects(Bucket=BUCKET_NAME, Prefix=video_dir_format(video_id))