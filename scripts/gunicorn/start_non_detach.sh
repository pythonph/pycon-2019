#!/bin/bash

DJANGO_SETTINGS=config.settings.production
DJANGO_WSGI=config.wsgi
SOCKFILE=/srv/funny/pycon/run/gunicorn.sock
PIDFILE=/srv/funny/pycon/run/gunicorn.pid
LOG_FILE=/srv/funny/pycon/logs/gunicorn.log
LOG_LEVEL=debug
NUM_WORKERS=3

# Delete any existing sock and pid files
rm -f $PIDFILE $SOCKFILE

echo "-> Starting gunicorn:edgepi as user funny"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS
export PYTHONPATH=/srv/funny/pycon:\$PYTHONPATH
exec gunicorn \
    ${DJANGO_WSGI}:application \
    --name happy \
    --user funny \
    --group funny \
    --workers $NUM_WORKERS \
    --bind=unix:$SOCKFILE \
    --log-level=$LOG_LEVEL \
    --log-file=$LOG_FILE \
    --pid=$PIDFILE \
