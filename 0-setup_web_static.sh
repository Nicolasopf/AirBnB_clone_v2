#!/usr/bin/env bash
# Setup installation, creating folders, install nginx, give ownerships and create symbolic links
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
link="/data/web_static/current"
rm -rf "$link"
ln -s /data/web_static/releases/test/ "$link"
echo "Holberton School" > /data/web_static/releases/test/index.html
str="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
if [ "$(grep -c "location /hbnb_static {" /etc/nginx/sites-available/default)" -eq 0 ]; then
    sed -i "45i $str" /etc/nginx/sites-available/default
fi
service nginx restart
