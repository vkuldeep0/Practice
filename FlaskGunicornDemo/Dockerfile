# Dockerfile
FROM python:3.11-slim

# Set Workdir
WORKDIR /app

# Install build deps and packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .
COPY gunicorn.conf.py .

# Expose ports that gunicorn will listen on
EXPOSE 8000

# The commandr runs gunicorn using the config file
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
