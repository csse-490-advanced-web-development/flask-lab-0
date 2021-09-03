# This code is from https://github.com/miguelgrinberg/flasky/blob/2a/hello.py
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World! I\'m [Your Name Goes Here]!</h1>'
