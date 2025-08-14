# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Ensure writable DB path
RUN mkdir -p /app/app/db

# Set environment variable for SQLite DB path
ENV SQLITE_PATH=/app/app/db/babybot.db

# Expose the port your app runs on
EXPOSE 8000

# Command to run the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
