"""Web Server Gateway Interface"""
import os
from src.app import app

#app.config.from_object(os.environ['APP_SETTINGS'])
if __name__ == '__main__':
    # DEV ENV
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
