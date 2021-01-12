## develop image
FROM python:3.8-slim AS develop

## install dependencies
RUN apt-get update
RUN apt-get install gcc python-psycopg2 libpq-dev python3-dev musl-dev -y

## set working directory
WORKDIR /usr/src/app

## add and install requirements
ADD . .
RUN pip3 install --upgrade pip; pip3 install pip-tools
RUN pip3 install -r requirements.txt

## add permissions
RUN chmod -R 777 .

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

## run entrypoint.sh
CMD ./entrypoint.sh