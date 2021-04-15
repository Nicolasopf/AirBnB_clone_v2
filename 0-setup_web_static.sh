#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
if [ ! -f "/data/web_static/releases/test/index.html" ]; then
    echo "Mock Page" > /data/web_static/releases/test/index.html
fi
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
str="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
if [ "$(grep -c "location /hbnb_static {" /etc/nginx/sites-available/default)" -eq 0 ]; then
    sed -i "45i $str" /etc/nginx/sites-available/default
fi
service nginx restart
