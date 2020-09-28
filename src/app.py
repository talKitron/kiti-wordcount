""" Flask Application """

#load libraries
import os
from flask import Flask
# load modules
from src.endpoints.wordcount import wordcount

# init Flask app
app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])


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
    return hello_name('World')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

#if __name__ == '__main__':
#    app.run()