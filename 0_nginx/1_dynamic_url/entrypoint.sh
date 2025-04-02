#!/bin/sh

BASE_URL="${MY_BASE_URL:-/ui}"

# Replace placeholder in index.html and nginx.conf
sed -i "s|__BASE_PATH__|$BASE_URL|g" /etc/nginx/conf.d/default.conf

# Start nginx
nginx -g "daemon off;"
