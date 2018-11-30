#!/bin/bash

# Clean any artifacts
echo "--> Cleaning artifacts"
cd /srv/funny/pycon && make clean


# Make sure that the docker container can write to these directories
echo "--> Updating permissions for docker access"
find /srv/funny/pycon -iname "migrations" -type "d" | xargs sudo chmod 777
sudo chmod 777 /srv/funny/pycon/run
sudo chmod 777 /srv/funny/pycon/logs
sudo chmod 777 /srv/funny/pycon/logs/*.log
sudo chmod 777 /srv/funny/pycon/pycon/static
sudo chmod 777 /srv/funny/pycon/pycon/media

# Apply migrations
echo "--> Applying migrations"
cd /srv/funny/pycon
source scripts/utils/django_manage.sh migrate
