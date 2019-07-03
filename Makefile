
docker-build:
	docker build -t crawl-image .

docker-run:	docker-build
	docker run crawl-image

build:
	pipenv install

run:
	pipenv run python3 src/main.py

cloud-build:
	gcloud builds submit --config cloudbuild.yaml .

# or without the config file
# gcloud builds submit --tag gcr.io/ev-crawl/crawl-image .
