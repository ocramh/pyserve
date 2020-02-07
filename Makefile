REDIS_IMAGE=redis:5.0.7-alpine
RABBITMQ_IMAGE=rabbitmq:3.8.2-alpine
APP_IMAGE=ocramh/celery

.PHONY: run-celery
run-celery: ## run celery task queue
	celery -A server.app worker --loglevel=info --concurrency=3

.PHONY: run-flask
run-flask: ## run the flask http server
	python main.py

.PHONY: docker-build
docker-build: ## builds the app docker images
	docker build -t ${APP_IMAGE}:latest .

.PHONY: run-rabbitmq
run-rabbitmq: ## starts a rabbitmq docker container
	docker run --rm -d \
	--name dvr-rabbit \
	--hostname dvr-rabbit \
	-p 5672:5672 \
	${RABBITMQ_IMAGE}