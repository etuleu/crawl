
docker-build:
	docker build -t simple-python-docker .

docker-run:	docker-build
	docker run simple-python-docker

build:
	pipenv install

run:
	pipenv run python3 src/main.py

cloud-build:
	gcloud builds submit --config cloudbuild.yaml .

# or without the config file
# gcloud builds submit --tag gcr.io/ev-crawl/crawl-image .
