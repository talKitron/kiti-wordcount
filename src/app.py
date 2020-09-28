""" Flask Application """

#load libraries
from flask import Flask

# init Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()