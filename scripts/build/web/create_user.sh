#!/bin/bash
APP_USER=funny
APP_HOME=/srv/funny
SUDO_USER=happy
SUDO_PASS=happy@1234


echo "--> Creating superuser '$SUDO_USER'"
sudo useradd --user-group --no-create-home \
      --shell /bin/bash \
          $SUDO_USER
echo $SUDO_USER:$SUDO_PASS | sudo chpasswd
sudo adduser $SUDO_USER sudo
echo "$SUDO_USER ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/90-cloud-init-users

echo "--> Creating application user '$APP_USER'"
sudo mkdir -p $APP_HOME
sudo useradd --system --user-group \
      --shell /bin/bash \
          --home-dir $APP_HOME \
              $APP_USER
sudo chown $APP_USER: $APP_HOME

echo "--> Updating user '$SUDO_USER' and '$APP_USER' groups"
sudo usermod -aG $APP_USER $SUDO_USER
sudo usermod -aG $SUDO_USER $APP_USER
