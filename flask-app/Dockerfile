# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Flask app
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port used by the Flask app
EXPOSE 8080

ARG VERSION=v1
ENV VERSION=${VERSION}

# Command to run the app
CMD ["python", "app.py"]
