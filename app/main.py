import os

from server.app import flask_app
from server.app import metrics

if __name__ == '__main__':
  # start flask server
  host = os.environ['SERVER_HOST']
  port = os.environ['SERVER_PORT']

  if "DEBUG" in os.environ:
    debug=True
  else:
    debug=False

  metrics.init_app(flask_app)
  flask_app.run(host=host, port=int(port), debug=debug)