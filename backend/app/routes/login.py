from flask import Blueprint, render_template, abort, request, jsonify
from flask_login import current_user, login_user, logout_user
from app.models import UserAccount, SubscriberRelationship

from ..helpers import db

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['POST'])
def login():

    if current_user.is_authenticated:
        return jsonify({
            'result': 'already'
        })

    user = UserAccount.query.filter_by(username=request.args.get('username')).first()
    if user is None or not user.check_password(request.args.get('password')):
        return jsonify({
            'result': 'login_failure'
        })

    login_user(user, remember=request.args.get('remember_me'))
    
    return jsonify({
        'result': 'login_success'
    })

@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({
        'result': 'logout_success'
    })

@bp.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return "already_registered"
    
    user = UserAccount(username=request.form['username'], email=request.form['email'])
    user.set_password(request.form['password'])
    db.session.add(user)
    db.session.commit()

    return "register_success"


@bp.route('/profile', methods=['GET'])
def profile():

    if current_user.is_authenticated:
        return jsonify({
            'logged_in': True,
            'username': current_user.username
        })

    return jsonify({
        'logged_in': False
    })

@bp.route('/subscribe', methods=['POST'])
def subscribe():

    if not current_user.is_authenticated:
        return jsonify({'result': "Not logged in."})

    channel_id = request.args.get('id')
    relationship = SubscriberRelationship(current_user.get_id(), channel_id)

    db.session.add(relationship)
    db.session.commit()

    return jsonify({'result': "Success"})

@bp.route('/unsubscribe', methods=['POST'])
def unsubscribe():

    if not current_user.is_authenticated:
        return jsonify({'result': "Not logged in."})

    channel_id = request.args.get('id')

    to_delete = SubscriberRelationship.query.filter_by(follower_id=current_user.get_id(), following_id=channel_id).first()
    to_delete.delete()

    db.session.commit()

    return jsonify({'result': "Success"})




    