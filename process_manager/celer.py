from celery import Celery

def celery_init(app):
  celery = Celery(
    app.import_name,
    broker=app.config['CELERY_BROKER_URL'],
    task_acks_late=True,
    reject_on_worker_lost=True
  )
  celery.conf.update(app.config)
  
  return celery