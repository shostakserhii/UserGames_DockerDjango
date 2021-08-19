#!/usr/bin/bash

python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

gunicorn --bind=127.0.0.1:8000 games.config.wsgi:app