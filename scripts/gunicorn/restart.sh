#!/bin/bash

cp scripts/conf/gunicorn.conf /etc/supervisor/conf.d/
. /srv/funny/env/venv/bin/activate
supervisorctl restart gunicorn
deactivate
