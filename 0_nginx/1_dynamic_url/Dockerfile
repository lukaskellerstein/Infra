FROM nginx:alpine

# Copy dist - SPA
COPY ./dist /usr/share/nginx/html/dist

# Copy nginx config
COPY nginx.conf.template /etc/nginx/conf.d/default.conf

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
