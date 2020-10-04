""" Flask Application """

# load libraries
import os
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy

# load modules
from src.endpoints.wordcount import wordcount

# load data models
from src.models import Result

# init Flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(wordcount)


@app.route('/env')
def env():
    if 'APP_SETTINGS' in os.environ:
        return "Current environment: {}".format(os.environ['APP_SETTINGS'])
    else:
        return 'APP_SETTINGS not loaded'


@app.route('/')
def home():
    return Response(hello_name('World'), 200)


@app.route('/<name>')
def hello_name(name):
    return Response("Hello {}!".format(name), 200)


if __name__ == '__main__':
    app.run()
