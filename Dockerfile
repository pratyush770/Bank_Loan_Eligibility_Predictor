# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all necessary files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 5000

# Command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
