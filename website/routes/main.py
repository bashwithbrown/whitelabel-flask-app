from flask import (Flask, url_for, redirect, Blueprint, render_template)
from core import config

main = Blueprint('main', __name__, static_folder='../static/', template_folder='../templates/main')

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.home'))


@main.route('/home', methods=['GET'])
def home():
    return render_template('home.html')