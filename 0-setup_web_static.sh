#!/usr/bin/env bash
# Setup installation, creating folders, install nginx, give ownerships and create symbolic links
apt update nginx
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
link="/data/web_static/current"

if [ -L $link ]; then
	rm -rf "$link"
fi

ln -s /data/web_static/releases/test/ "$link"
echo "Holberton School" > /data/web_static/releases/test/index.html
chown -R ubuntu:ubuntu /data/
if [[ $(grep -c "alias /data/web_static/current" /etc/nginx/sites-available/default) -ge 1 ]]; then
	sed -i '/server_name _;/a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/\n\t}' /etc/nginx/sites-available/default
fi
service nginx restart
