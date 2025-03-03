# Joel Javier De Alba MSc BSc CS | 2025-02-03 March 2025
# Dockerfile for the Flask backend of the Py_Flask_Bken_Dev_2025 project

# Use the latest Ubuntu image
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy backend files
COPY py_flsk_bken_dev_2025 /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install flask Flask-PyMongo Flask-WTF

# Expose backend port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "run.py"]

# End of Dockerfile
