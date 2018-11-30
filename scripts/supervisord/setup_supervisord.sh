
echo 'Creating virtual environment for supervisord'
pip install virtualenv
virtualenv --python=/usr/bin/python2.7 /srv/funny/env/venv
. /srv/funny/env/venv/bin/activate

echo 'Installing supervisord'
pip install supervisor

echo 'Moving supervisord conf'
mkdir -p /etc/supervisor/conf.d
cp /srv/funny/pycon/scripts/conf/supervisord.conf /etc/supervisor/
chmod 644 /etc/supervisor/supervisord.conf
supervisord
deactivate
