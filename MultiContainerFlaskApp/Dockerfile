# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the app code
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
