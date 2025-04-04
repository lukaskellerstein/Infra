#!/bin/sh

# Default to 7600 if PORT is not set
PORT="${PORT:-7600}"

echo "Starting HTTP server on port $PORT..."
exec python -m http.server "$PORT" --bind 0.0.0.0
