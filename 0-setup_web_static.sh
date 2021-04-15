#!/usr/bin/env bash
# Script for preparing deployment of web_static on the servers.
# Install nginx. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
#
# Check if nginx default config file exists.
if [[ ! -e /etc/nginx/sites-available/default ]]; then
    # update and install if no file exists.
    apt-get update && apt-get install nginx -y
fi

# Create /data/web_static/releases/test and /shared directories. - - - - - - -|
if [[ ! -e /data/web_static/releases/test ]]; then
    # Recursively create test dir.
    mkdir -p /data/web_static/releases/test
fi
if [[ ! -e /data/web_static/shared ]]; then
    mkdir -p /data/web_static/shared
fi

# Create dummy .html file - - - - - - - - - - - - - - - - - - - - - - - - - - |
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link. - - - - - - - - - - - - - - - - - - - - - - - - - - - |
#
# Remove symlink file if it exists.
if [[ -e /data/web_static/current ]]; then
    rm /data/web_static/current
fi
# Create symlink file again.
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change user and group of /data/*.  - - - - - - - - - - - - - - - - - - - - - |
chown -R ubuntu:ubuntu /data/

# Add /hbnb_static location on nginx's default file. - - - - - - - - - - - - -|
# if ! grep -q "hbnb_static" /etc/nginx/sites-available/default; then
#     Line='\\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}'
#     sed -i "37i $Line" /etc/nginx/sites-available/default
# fi

# Restart nginx's service. - - - - - - - - - - - - - - - - - - - - - - - - - -|
service nginx restart
