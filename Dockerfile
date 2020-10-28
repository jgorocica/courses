FROM python:3.8.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
libmariadb-dev python-dev libgtk-3-dev build-essential

ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/