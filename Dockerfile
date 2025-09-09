# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the app files into the container
COPY . .

# Install Flask and other required dependencies
RUN pip install Flask

# Run the application
CMD ["python", "app.py"]
