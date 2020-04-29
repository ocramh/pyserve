REDIS_IMAGE=redis:5.0.7-alpine
RABBITMQ_IMAGE=rabbitmq:3.8.2-alpine

.PHONY: setup
setup:
	./scripts/env.sh

.PHONY: run-rabbitmq
run-rabbitmq: ## starts a rabbitmq docker container
	docker run --rm -d \
	--name rabbitmq \
	--hostname rabbitmq \
	-p 5672:5672 \
	${RABBITMQ_IMAGE}

.PHONY: run-dramatiq
run-dramatiq: ## run dramatiq task queue
	dramatiq app 

.PHONY: run-flask
run-flask: ## run the flask http server
	python main.py

.PHONY: clean
clean: ## run the flask http server
	conda deactivate dramatiq-test
	conda env remove --name dramatiq-test