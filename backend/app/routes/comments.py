from flask import Blueprint, render_template, abort, request, jsonify
from flask_login import current_user, login_user, logout_user
from app.models import UserAccount, SubscriberRelationship, VideoComment
import datetime

from ..helpers import db, easy_date_format

bp = Blueprint('comments', __name__)

@bp.route('/submit_comment', methods=['POST'])
def submit_comment():
    
    if not current_user.is_authenticated:
        return jsonify({'result': "Not logged in."})

    user_id = current_user.get_id()
    video_id = request.args.get('video_id')
    content = request.args.get('content')
    post_time = datetime.datetime.now()

    comment = VideoComment(user_id=user_id, video_id=video_id, content=content, post_time=post_time)

    db.session.add(comment)
    db.session.commit()

    return jsonify({
        'result': 'Success',
        'data': {
        }
    })

@bp.route('/edit_comment', methods=['POST'])
def edit_comment():
    comment_id = request.args.get('id')

    if not current_user.is_authenticated:
        return jsonify({'result': 'Not logged in.'})

    comment = VideoComment.query.filter_by(id=comment_id).first()

    if comment.user_id != current_user.get_id():
        return jsonify({'result': 'No access to this comment'})


@bp.route('/get_comments', methods=['GET'])
def get_comments():

    start = request.args.get('start')
    num = request.args.get('num')
    video_id = request.args.get('video_id')

    comments = VideoComment.query.filter_by(video_id=video_id).limit(num).offset(start).all()

    to_return = []

    for row in comments:
        user = UserAccount.query.filter_by(id=row.user_id).first()

        to_return.append({
            'username': user.username,
            'channel_url': user.channel_url,
            'channel_icon_url': user.channel_icon_url,
            'content': row.content,
            'post_time': row.post_time if row.post_time is None else easy_date_format(datetime.datetime.now() - row.post_time)
        })

    return jsonify({
        "data": to_return
    })
        