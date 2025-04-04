FROM debian:bullseye-slim

# Set environment variables to make things non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update base and install common tools
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    bash \
    vim \
    nano \
    less \
    htop \
    netcat-traditional \
    iproute2 \
    iputils-ping \
    dnsutils \
    procps \
    net-tools \
    jq \
    git \
    unzip \
    lsof \
    telnet \
    tree \
    rsync \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js 18 and npm from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Use bash by default
CMD ["bash"]
