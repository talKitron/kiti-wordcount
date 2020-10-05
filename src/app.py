""" Flask Application """

# load libraries
import os
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy

# init Flask app
app = Flask(__name__, template_folder='templates')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# load modules
from src.endpoints.wordcount import wordcount

# load data models - moved to wordcount.py
# from src.models import Result

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(wordcount)


@app.route('/env')
def env():
    if 'APP_SETTINGS' in os.environ:
        return "Current environment: {}".format(os.environ['APP_SETTINGS'])
    else:
        return 'APP_SETTINGS not loaded'


# @app.route('/')
# def home():
#     return hello_name('World')
@app.route('/<name>')
def hello_name(name):
    return Response("Hello {}!".format(name), 200)


if __name__ == '__main__':
    app.run()
