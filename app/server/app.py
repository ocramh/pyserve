import os
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from process_manager import celer, tasks

flask_app = Flask(__name__)

# add prometheus exporter
metrics = PrometheusMetrics(app=None, path='/metrics')
metrics.info('app_info', 'Application info', version='1.0.3')

# configure celery
flask_app.config.update(
  CELERY_BROKER_URL=os.environ['CELERY_BROKER_URL'],
)
workers = celer.celery_init(flask_app)

# celery tasks
@workers.task(acks_late=True, reject_on_worker_lost=True)
def test_task():
  return tasks.test_task()

# routes
@flask_app.route('/')
@metrics.summary('requests_by_status', 'Request latencies by status', labels={'status': lambda r: r.status_code})
def home():
  return 'ok'

@flask_app.route('/process')
def process():
  test_task.apply_async()
  return 'processing async task'
