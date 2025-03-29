# -------------------------------
# Stage 1: Build the app
# -------------------------------
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY package*.json ./
RUN npm ci

# Copy the rest of the app source code
COPY . .

# Build the app
RUN npm run build

# -------------------------------
# Stage 2: Serve the built app with Nginx
# -------------------------------
FROM nginx:alpine

# Copy the build output to Nginx's web directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx config (optional)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
