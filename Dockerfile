# Use an official Python base image
FROM python:3.10.1-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code and requirements into the container
COPY requirements.txt .
COPY whatsappreminder.py .
COPY test.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional, use .env file if you have secrets)
# ENV CANVAS_API_KEY=your_key_here
# ENV WHATSAPP_PHONE=your_phone
# ENV CALLMEBOT_API_KEY=your_apikey

# Make sure we have the .env file if needed
COPY .env .env

# Run the script when the container starts
CMD ["python", "whatsappreminder.py"]
