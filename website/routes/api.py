import os
import json
import datetime as dt

from werkzeug.utils import secure_filename

from flask import (Flask, render_template, request, url_for, redirect, flash, Blueprint)
from flask_login import login_required, current_user, login_user

from core import config
from functions import *
from database import DatabaseManager


api = Blueprint('api', __name__)
logger = Logger(config)
database_manager = DatabaseManager(config.DATABASE)


# start: USER
@api.route('alter-user-information/<string:user_id>', methods=['POST'])
def alter_user_information(user_id):
    username = request.form['username']
    email = request.form['email']
    is_admin = request.form.get('is_admin')
 
    try:
        with database_manager as session:
            user = session.query(database_manager.User).filter_by(id=user_id).first()
            user.username = username
            user.meta_data = json.loads(user.meta_data)
            user.meta_data['is_admin'] = 'True' if is_admin else "False"
            user.meta_data = json.dumps(user.meta_data)
            session.commit()

        return redirect(url_for('user.index'), code=302)

    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('user.index'), code=302)


@api.route('/alter-user-profile-picture/<string:user_id>', methods=['POST'])
@login_required
def alter_user_profile_picture(user_id):
    try:

        file = request.files['file']
        if not allowed_file(file.filename, config.ALLOWED_EXTENSIONS):
            flash('File type not allowed.', 'error')
            return redirect(url_for('user.profile'), code=302)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(config.FILE_UPLOAD_DIR, filename))

            with database_manager as session:
                user = session.query(database_manager.User).filter_by(id=user_id).first()

                user.meta_data = json.loads(user.meta_data)
                user.meta_data['profile_picture'] = filename
                user.meta_data = json.dumps(user.meta_data)
                session.commit()

            return redirect(url_for('user.profile'), code=302)

    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('user.profile'), code=302)
# end: USER

# start: AUTH
@api.route('/login-user', methods=['POST'])
def login_user_profile():
    try:
        with database_manager as session:
            user = session.query(database_manager.User).filter_by(username=request.form.get("username")).first()

            if user and user.password == request.form.get("password"):
                login_user(user, remember=bool(request.form.get('remember')))

                user.meta_data = json.loads(user.meta_data)
                user.meta_data.update({
                    'last_login_datetime': str(dt.datetime.now()),
                    'last_login_user_info': {
                        'remote_addr': request.remote_addr,
                        'x_forwarded_for': request.headers.get('X-Forwarded-For')
                    }
                })
                user.meta_data = json.dumps(user.meta_data)
                session.commit()

                flash('You were successfully logged in')
                return redirect(url_for('main.index'))
            else:
                flash('Wrong username or password.', 'error')
                return redirect(url_for('auth.login'))
    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('main.index'), code=302)

@api.route('/signup-user', methods=['POST'])
def signup_user():
    try:
        with database_manager as session:
            user = session.query(database_manager.User).filter_by(username=request.form.get('username')).first()

        if user:
            flash('username taken.', 'error')
            return redirect(url_for('auth.signup'))
        else:
            with database_manager as session:
                new_user = database_manager.User(
                    id=generate_id('uuid'),
                    username=request.form.get('username'),
                    password=request.form.get('password'),
                    meta_data=json.dumps({'email': request.form.get('email'), "is_admin": "False"}))

                session.add(new_user)
                session.commit()

            return redirect(url_for('auth.login'))

    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('main.index'), code=302)

@api.route('alter-user-password/<string:user_id>', methods=['POST'])
def alter_user_password(user_id):
    try:
        with database_manager as session:
            user = session.query(database_manager.User).filter_by(id=user_id).first()

            current_password = request.form['current_password']
            new_password = request.form['new_password']
            new_password_2 = request.form['new_password_2']

            if current_password != user.password:
                flash('Incorrect password', 'error')
            elif new_password != new_password_2:
                flash('New passwords don\'t match', 'error')
            elif len(new_password) <= 4:
                flash('Password length has to be greater than 4.', 'error')
            elif current_password == new_password:
                flash('New password cannot be the same as the current one.', 'error')
            else:
                user.password = new_password
                session.commit()
                flash('Password has successfully been changed')
                return redirect(url_for('user.profile'), code=302)

            return redirect(url_for('auth.reset_password'), code=302)

    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('main.index'), code=302)
# end: AUTH

# start: SERVER
@api.route('/delete-file/<string:file_name>', methods=['POST'])
@login_required
def delete_file(file_name):
    try:
        os.remove(os.path.join(config.FILE_UPLOAD_DIR, file_name))
        flash(f'{file_name} deleted successfully')
        return redirect(url_for('admin.index'), code=302)

    except Exception as exc:
        log_api_error(logger, exc, request)
        return redirect(url_for('admin.index'), code=302)
# end: SERVER