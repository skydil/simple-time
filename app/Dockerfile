# Use an official Python runtime as a parent image
FROM python:3.12.2-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP=main.py

# Run Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]

