"""Web Server Gateway Interface"""
import os
from src.app import app

if __name__ == '__main__':
    #DEV ENV
    app.config.from_object(os.environ['APP_SETTINGS'])
    #app.run(host='0.0.0.0', debug=True)