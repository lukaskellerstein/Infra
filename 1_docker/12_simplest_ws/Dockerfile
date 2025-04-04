FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir websockets

COPY server.py .

# Use environment variable to define the port
ENV PORT=8765

CMD ["python", "server.py"]
