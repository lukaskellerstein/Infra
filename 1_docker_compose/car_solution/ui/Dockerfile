# Use an official Python image with Python 3.12
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install uv - fast Python package manager
RUN curl -Ls https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Verify uv
RUN which uv && uv --version

# Copy project files
COPY . .

# Create uv virtual environment
RUN uv venv
# Install dependencies using uv sync
RUN uv sync


# ------------------------------
RUN echo "Working directory:" && pwd
RUN echo "Contents of current folder:" && ls -al .
# ------------------------------
    
# Expose the port uvicorn will run on
EXPOSE 8000

CMD ["uv", "run", "main.py"]
