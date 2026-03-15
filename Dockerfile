FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create directories for media, static and data
RUN mkdir -p media static data

EXPOSE 8000

# Production command using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8004", "--workers", "3", "--threads", "2", "--worker-class", "gthread", "--worker-tmp-dir", "/dev/shm", "--timeout", "60", "backend.wsgi:application"]
