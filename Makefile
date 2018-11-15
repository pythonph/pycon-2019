SHELL := /bin/bash

.PHONY:
		build

build:
		venv requirements.txt
		venv/bin/pip-sync

venv:
		python3 -m venv venv
		venv/bin/pip install pip-tools

requirements.txt:
		requirements.in
		venv/bin/pip-compile requirements.in > requirements.txt

clean:
		find . -iname "*.pyc" | xargs rm -Rf
		find . -iname "*.pyo" | xargs rm -Rf
		find . -iname "*.pyd" | xargs rm -Rf
		find . -iname "__pycache__" | xargs rm -Rf

build_base:
		pip3 install -r requirements/production.txt

init_env:
		make clean
		make build_base
		source scripts/build/web/create_user.sh

deploy:
		make build_base
		source scripts/utils/django_manage.sh collectstatic
		source scripts/utils/django_manage.sh migrate
		make gunicorn_start

gunicorn_start:
		source scripts/gunicorn/start.sh

gunicorn_stop:
		source scripts/gunicorn/stop.sh

gunicorn_restart:
		source scripts/gunicorn/restart.sh
