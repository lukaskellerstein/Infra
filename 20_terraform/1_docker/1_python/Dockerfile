FROM python:3.11-slim

WORKDIR /app

COPY script/app.py .

# -u flag is used to force the stdout and stderr streams to be unbuffered
CMD ["python", "-u", "app.py"]
