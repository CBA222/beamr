from flask import Blueprint, render_template, abort, request, jsonify
from app.models import Video, UserAccount

from ..helpers import db

bp = Blueprint('videos', __name__)

@bp.route('/video', methods=['GET'])
def video():
    result_video = Video.query.filter_by(id=request.args.get('id')).first()
    result_channel = UserAccount.query.filter_by(id=result_video.channel_id).first()

    return {
        "manifest_url": result_video.manifest_url,
        "title": result_video.title,
        "channel": result_channel.username,
        "channel_url": result_channel.channel_url,
        "channel_icon_url": result_channel.channel_icon_url,
        "view_count": result_video.view_count,
        "upload_date": result_video.upload_date,
        "subscriber_count": result_channel.subscriber_count,
        "description": result_video.description
    }

@bp.route('/upnext_videos', methods=['GET'])
def upnext_videos():
    start = request.args.get('start')
    num = int(request.args.get('num'))

    results = Video.query.limit(num).offset(start).all()
    channel_ids = [x.channel_id for x in results]

    channel_dict = dict()

    for x in channel_ids:
        channel = UserAccount.query.filter_by(id=x).first()
        channel_dict[x] = channel

    to_return = []

    return {
        'videos': [
            {
                "static_url": item.thumbnail_url,
                "animated_url": item.thumbnail_url,
                "title": item.title,
                "channel": channel_dict[item.channel_id].username,
                "channel_url": channel_dict[item.channel_id].channel_url,
                "view_count": item.view_count,
                "upload_date": item.upload_date,
                "video_length": "5:34",
                "video_url": "watch?id={}".format(item.id)
            }
            for item in results
        ]
    }

@bp.route('/home_videos', methods=['GET'])
def home_videos():
    start = request.args.get('start')
    num = int(request.args.get('num'))

    results = Video.query.limit(num).offset(start).all()

    to_return = []

    return {
        'videos': [
            {
                "static_url": item.thumbnail_url,
                "animated_url": item.thumbnail_url,
                "title": item.title,
                "channel": "doctordoom",
                "channel_url": "",
                "view_count": item.view_count,
                "upload_date": item.upload_date,
                "video_length": "5:34",
                "video_url": "watch?id={}".format(item.id)
            }
            for item in results
        ]
    }