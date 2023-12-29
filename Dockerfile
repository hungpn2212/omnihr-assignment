FROM python:3.10 AS build

COPY requirements.txt ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


FROM python:3.10 AS runtime

ENV APP_HOME /app
ENV APP_USER app
ENV APP_GRP app
ENV APP_SHELL /sbin/nologin

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN groupadd "${APP_GRP}" \
&&  useradd --create-home --home-dir "${APP_HOME}" --shell "${APP_SHELL}" --gid "${APP_GRP}" "${APP_USER}" \
&&  chown -R "${APP_USER}":"${APP_GRP}" "${APP_HOME}"

RUN apt-get -y update && apt-get -y install gdal-bin libmagic1 libxml2 binutils libproj-dev

COPY . .
