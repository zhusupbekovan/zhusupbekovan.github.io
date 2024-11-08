# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install psycopg2-binary

# Copy script to container
COPY my_data_generator.py /app/

# Run the script
CMD ["python", "data_generator.py"]
