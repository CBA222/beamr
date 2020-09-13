from fastapi import APIRouter, HTTPException
import time
from sqlalchemy import text, create_engine

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

router = APIRouter()

@router.get("/video")
async def video(video_id: int = 0):
    conn = get_sql_connection()
    stmt = text("SELECT * FROM video WHERE id=:p1;")
    stmt = stmt.bindparams(p1=video_id)
    result_video = conn.execute(stmt).fetchone()

    stmt = text("SELECT * FROM channel WHERE id=:p1;")
    stmt = stmt.bindparams(p1=result_video["channel_id"])
    result_channel = conn.execute(stmt).fetchone()
    conn.close()

    return {
        "manifest_url": result_video["manifest_url"],
        "title": result_video["title"],
        "channel": result_channel["name"],
        "channel_url": result_channel["channel_url"],
        "channel_icon_url": result_channel["channel_icon_url"],
        "view_count": result_video["view_count"],
        "upload_date": result_video["upload_date"],
        "video_id": video_id,
        "subscriber_count": result_channel["subscriber_count"],
        "description": result_video["description"]
    }

@router.get("/upnext_videos")
async def upnext_videos(start: int, num: int):
    to_return = []

    for i in range(num):
        to_return.append({
            "static_url": "https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/static.webp",
            "animated_url": "https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/animated.webp",
            "title": "A Cat Video",
            "channel": "doctordoom",
            "channel_url": "",
            "view_count": 123798,
            "upload_date": "Nov 29, 2015",
            "video_length": "5:34",
            "video_url": "watch?id=3"
        })

    return {
        "videos": to_return
    }

@router.get("/home_videos")
async def home_videos(start: int, num: int):
    to_return = []

    for i in range(num):
        to_return.append({
            "static_url": "https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/static.webp",
            "animated_url": "https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/animated.webp",
            "title": "A Cat Video",
            "channel": "doctordoom",
            "channel_url": "",
            "view_count": 123798,
            "upload_date": "Nov 29, 2015",
            "video_length": "5:34",
            "video_url": "watch?id=4"
        })

    time.sleep(1.5)

    return {
        "videos": to_return
    }