#!/bin/bash

echo "Installing and setting up supervisord"
source /srv/funny/pycon/scripts/supervisord/setup_supervisord.sh

source /srv/funny/pycon/scripts/utils/setup_env.sh

cd /srv/funny/pycon && make deploy

export DJANGO_READ_DOT_ENV_FILE=true

echo "--> [default] Starting ssh service"
/usr/sbin/sshd -D
