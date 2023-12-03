# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install build dependencies for uWSGI
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install uWSGI
RUN pip install uwsgi

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py using uWSGI when the container launches
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "app:app"]
