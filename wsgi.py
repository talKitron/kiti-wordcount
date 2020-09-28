"""Web Server Gateway Interface"""

from src.app import app

if __name__ == '__main__':
    #DEV ENV
    app.run(host='0.0.0.0', debug=True)