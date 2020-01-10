import os
import logging
from flask import Flask

from process_manager import celer, tasks

flask_app = Flask(__name__)

flask_app.config.update(
  CELERY_BROKER_URL=os.environ['CELERY_BROKER_URL'],
)

workers = celer.celery_init(flask_app)

# celery tasks
@workers.task(acks_late=True, reject_on_worker_lost=True)
def test_task():
  return tasks.test_task()

@flask_app.route('/')
def home():
  return 'ok'

@flask_app.route('/process')
def process():
  test_task.apply_async()
  return 'processing async task'
  
