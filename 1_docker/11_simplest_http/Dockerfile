FROM python:3.12-slim

# Install tools
RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    nodejs \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run entrypoint that uses env var
CMD ["/entrypoint.sh"]
