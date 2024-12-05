import psycopg2
from confluent_kafka import Consumer
import json
from  config.kafka_config import CONSUMER_CONFIG

# PostgreSQL Connection
pg_config = {
    'host': 'localhost',
    'database': 'test',
    'user': 'admin',
    'password': 'admin'
}

def connect_to_postgres():
    return psycopg2.connect(**pg_config)

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        timestamp TIMESTAMP,
        device_id INTEGER,
        temperature FLOAT,
        humidity FLOAT,
        pressure FLOAT
    )
    """)
    conn.commit()

def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO sensor_data 
    (timestamp, device_id, temperature, humidity, pressure)
    VALUES (%s, %s, %s, %s, %s)
    """, (
        data['timestamp'], 
        data['device_id'], 
        data['temperature'], 
        data['humidity'], 
        data['pressure']
    ))
    conn.commit()

def consume_and_store():
    consumer = Consumer(CONSUMER_CONFIG)
    consumer.subscribe(['sensor_data'])

    conn = connect_to_postgres()
    create_table(conn)

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f'Error: {msg.error()}')
                continue

            data = json.loads(msg.value().decode('utf-8'))
            insert_data(conn, data)
            print(f"Inserted data: {data}")

    except KeyboardInterrupt:
        consumer.close()
        conn.close()

if __name__ == '__main__':
    consume_and_store()