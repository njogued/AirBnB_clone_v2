#!/usr/bin/env bash
# Script to install nginx if not installed
# Create several folders
# Create a html document
# Create a symbolic link
# Chown
# Update nginx configuration
# Restart the server

if ! which nginx > /dev/null 2>&1
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create the folders and html file
mkdir -p /data/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<!DOCTYPE html>\n<html lang="en">\n  <head></head>\n    <body>ALX is doing hard things to me</body>\n</html>" >> /data/web_static/releases/test/index.html

# Symbolic link
ln -sf /data/web_static/current /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
