#!/usr/bin/env bash
# Install Nginx if not already installed

if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "Hello, this is a test!" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_path="/etc/nginx/sites-available/default"
sed -i "/^\s*location \/hbnb_static {/!b;n;c\ \talias /data/web_static/current/;" $config_path

# Restart Nginx
service nginx restart

exit 0
