# CONTAINER_NAME = chute-and-ladder-python
# WORK_DIR = /src

# .PHONY: enter-runtime
# enter-runtime:
# 	docker run --rm -it \
# 	-v ${PWD}/src:${WORK_DIR} \
# 	--name ${CONTAINER_NAME} \
# 	-w=${WORK_DIR} \
# 	python:3-alpine \
# 	ash
# 	# -u 1000:1000 \

.PHONY: docker_build
docker_build:
	@docker-compose build

.PHONY: docker_enter
docker_enter:
	@docker-compose up -d
	@echo Starting docker container
	@echo Run this command next: pipenv shell
	@echo For the first run, run this command after the last command: pipenv install
	@docker-compose exec python-runtime bash

.PHONY: docker_stop
docker_stop:
	@docker-compose down

.PHONY: python_run
python_run:
	@cd src && python -m v1.main

.PHONY: python_test
python_test:
	@cd src && python -m unittest
