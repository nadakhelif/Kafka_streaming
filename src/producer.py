import json
import time
from confluent_kafka import Producer
from data_generator import DataGenerator
from config.kafka_config import PRODUCER_CONFIG

producer = Producer(PRODUCER_CONFIG)
topic = 'sensor_data'

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')

def produce_data():
    while True:
        # Use the DataGenerator method
        data = DataGenerator.generate_sensor_data()
        
        try:
            producer.produce(
                topic, 
                key=str(data['timestamp']), 
                value=json.dumps(data).encode('utf-8'),
                callback=delivery_report
            )
            producer.poll(0)
            time.sleep(10)
        except Exception as e:
            print(f"Error producing message: {e}")

if __name__ == '__main__':
    produce_data()