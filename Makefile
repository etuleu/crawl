
docker-build:
	docker build -t simple-python-docker .

docker-run:	docker-build
	docker run simple-python-docker

build:
	pipenv install

run:
	pipenv run python3 src/main.py
