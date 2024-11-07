# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install psycopg2-binary

# Copy script to container
COPY sensor_data_generator.py /app/

# Run the script
CMD ["python", "sensor_data_generator.py"]
