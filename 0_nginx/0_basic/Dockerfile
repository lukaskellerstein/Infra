FROM nginx:alpine

# Copy test index.html
COPY ./my_index.html /usr/share/nginx/html/test/my_index.html

# Copy test simple.html
COPY ./simple.html /usr/share/nginx/html/simple-page/simple.html

# Copy dist - SPA 1
COPY ./dist /usr/share/nginx/html/dist

# Copy dist2 - SPA 2
COPY ./dist2 /usr/share/nginx/html/dist2


COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
