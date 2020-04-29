import os

from app import flask_app

if __name__ == '__main__':
    # start flask server
    host = os.environ['SERVER_HOST']
    port = os.environ['SERVER_PORT']
    flask_app.run(host=host, port=int(port))
