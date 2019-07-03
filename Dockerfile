FROM python:alpine3.7

RUN apk add --no-cache git
RUN apk add --no-cache bash

RUN pip install pipenv

COPY . /app

WORKDIR /app

RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python3", "src/main.py"]
