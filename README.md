# PYServe

PYServe is a dummy project used for testing out a monitored enviroment composed of
- a python service using [flask](https://www.palletsprojects.com/p/flask/)
- a distributed task manager using [celery](http://www.celeryproject.org/) and [rabbitmq](https://www.rabbitmq.com/)

Monitoring is provided by [prometheus](https://prometheus.io/) and metrics displayed via [grafana](https://grafana.com/).

## Setup

Use docker-compose to bring the system up and running

```
docker-compose up
```
This will mount the application folder inside the flask container to make local developemnt easier.
By defualt:
- the flask app will be availbale at http://localhost:9797 and expose a /metric endpoint
- the promethus server will run at http://localhost:9191/
- the grafana dashboard will be available at http://localhost:3131/
