# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY backend/requirements.txt /app/

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container at /app
COPY backend /app

# Run the Flask application
CMD ["python", "app.py"]
