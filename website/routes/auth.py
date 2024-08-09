from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, login_user

from core import config
from functions import *

auth = Blueprint('auth', __name__, static_folder='../static/', template_folder='../templates/auth')
logger = Logger(config)

@auth.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/reset-password', methods=['GET'])
@login_required
def reset_password():
    return render_template('reset-password.html', methods=['GET'])