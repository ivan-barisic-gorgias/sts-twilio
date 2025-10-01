FROM python:3.11-slim

WORKDIR /app

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY *.py .

# Expose the port the app runs on
EXPOSE 5001

# Run the server
CMD ["python", "server.py"]
