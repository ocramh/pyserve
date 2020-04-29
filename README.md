# Flask-Celery

Experimenting with background task queues behind a flask server.

## Setup

Requires conda and docker.

1. export environment variables

```
source .env
```

2. create conda environment, activate it and install deps

```
make setup
```

3. start rabbitmq

```
make run-rabbitmq
```

4. start celery server at localhost:8787

```
make run-flask
```

5. in a new command line window

```
make run-dramatiq
```

6. start sending requests to the server to start background processes

```
curl 0.0.0.0:8787
```
