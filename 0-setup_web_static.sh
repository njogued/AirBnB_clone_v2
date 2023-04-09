#!/usr/bin/env bash
# Script to install nginx if not installed
# Create several folders
# Create a html document
# Create a symbolic link
# Chown -R user:group
# Update nginx configuration
# Restart the server

if ! which nginx > /dev/null 2>&1
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create the folders and html file
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<DOCTYPE html>
<html>
	<head></head>
	<body>ALX is doing hard things to me</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
