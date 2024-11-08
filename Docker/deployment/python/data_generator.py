import os
import psycopg2
import random
import time

# Database connection details
db_host = os.getenv('DB_HOST', 'localhost')
db_name = os.getenv('DB_NAME', 'my_data')
db_user = os.getenv('DB_USER', 'user')
db_password = os.getenv('DB_PASSWORD', 'password')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password
)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS my_data (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        sensor_value FLOAT
    )
""")
conn.commit()

# Generate and insert sensor data
try:
    while True:
        sensor_value = round(random.uniform(20.0, 30.0), 2)  # Random temperature data
        cur.execute("INSERT INTO my_data (sensor_value) VALUES (%s)", (sensor_value,))
        conn.commit()
        print(f"Inserted sensor value: {sensor_value}")
        time.sleep(5)  # Insert data every 5 seconds
except KeyboardInterrupt:
    pass
finally:
    cur.close()
    conn.close()
