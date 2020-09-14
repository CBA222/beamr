from flask import Blueprint, render_template, abort, request, jsonify
from flask_login import current_user, login_user, logout_user
from app.models import UserAccount, SubscriberRelationship

from ..helpers import db

bp = Blueprint('search', __name__)

@bp.route('/search', methods=['GET'])
def search():
    to_return = []
    num = int(request.args.get('num'))
    query = request.args.get('q')

    for i in range(num):
        to_return.append({
            'title': query,
            'view_count': 123123,
            'upload_date': '',
            'video_length': '5:65',
            'static_url': '#',
            'animated_url': '#',
            'channel': 'TaylorSwiftVEVO',
            'video_url': '#'
        })

    return jsonify({'data': to_return})