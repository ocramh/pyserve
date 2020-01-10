REDIS_IMAGE=redis:5.0.7-alpine
RABBITMQ_IMAGE=rabbitmq:3.8.2-alpine

.PHONY: run-celery
run-celery: ## run celery task queue
	celery -A server.app worker --loglevel=info --concurrency=3 

.PHONY: run-flask
run-flask: ## run the flask http server
	python main.py

.PHONY: run-redis
run-redis: ## starts a redis docker container
	docker run --rm -d \
	--name dvr-redis \
	-p 6379:6379 \
	${REDIS_IMAGE} redis-server --appendonly yes

.PHONY: run-rabbitmq
run-rabbitmq: ## starts a rabbitmq docker container
	docker run --rm -d \
	--name dvr-rabbit \
	--hostname dvr-rabbit \
	-p 5672:5672 \
	${RABBITMQ_IMAGE}