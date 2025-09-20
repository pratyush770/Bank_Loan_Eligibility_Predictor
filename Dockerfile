# Stage 1: Build the application with all dependencies
FROM python:3.11 as builder

# Set working directory in the build stage
WORKDIR /app

# Copy only the requirements file first to leverage Docker's cache
COPY requirements.txt .

# Install dependencies in the build stage
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Create a minimal production image
FROM python:3.11-slim

# Set working directory in the final image
WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application code from the current directory
COPY . .

# Expose Streamlit port
EXPOSE 5000

# Command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
