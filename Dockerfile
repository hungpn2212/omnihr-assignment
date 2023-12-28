FROM python:3.10 AS build

COPY requirements.txt ./

RUN python -m venv venv
RUN . venv/bin/activate && \
    (pip install -r requirements.txt)

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN apt-get -y update && apt-get -y --qq install gdal-bin libmagic1 libxml2 binutils libproj-dev

COPY . .

EXPOSE 5000
