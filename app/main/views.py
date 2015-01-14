from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/hours-and-directions')
def hours():
    return render_template('hours-and-directions.html')
