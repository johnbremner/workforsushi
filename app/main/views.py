from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about-robata-grill')
def about():
    return render_template('about.html')

@main.route('/robata-grill-menu')
def menu():
    return render_template('menu.html')
