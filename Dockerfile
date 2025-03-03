# Joel Javier De Alba MSc BSc CS | 2025-02-03 March 2025
# Dockerfile for the Flask backend of the Py_Flask_Bken_Dev_2025 project

# Use the latest Ubuntu image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy backend files to container
COPY py_flsk_bken_dev_2025 /app

# Install Python dependencies
RUN pip install --no-cache-dir --break-system-packages -r /app/requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python3", "run.py"]


# End of Dockerfile
