FROM python:3.10-slim

WORKDIR /usr/src/app

COPY wait-for-it.sh /usr/bin/

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential gettext libpq-dev git python3-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pipenv==2020.8.13 pip setuptools wheel

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --ignore-pipfile --dev

COPY .. .

CMD python manage.py runserver 0.0.0.0:8000
