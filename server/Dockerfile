FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies for GDAL
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    gcc \
    g++ \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Set GDAL environment variables
ENV GDAL_VERSION $(gdal-config --version)
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install GDAL Python bindings
RUN pip install GDAL==$GDAL_VERSION

# Continue with your application setup
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# Run the application
CMD gunicorn jobs-app.wsgi:application --bind 0.0.0.0:$PORT
