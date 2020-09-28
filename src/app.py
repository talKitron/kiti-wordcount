""" Flask Application """

#load libraries
from flask import Flask
# load modules
from src.endpoints.wordcount import wordcount

# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(wordcount)

@app.route('/')
def home():
    return hello_name('World')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()