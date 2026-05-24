#!/bin/bash

echo "[1] Creating Dockerfile..."

cat << 'DOCKER' > Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    libjpeg-dev \\
    zlib1g-dev \\
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 8080

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Default command
ENTRYPOINT ["/app/entrypoint.sh"]
DOCKER

echo "[DONE] Dockerfile created."
