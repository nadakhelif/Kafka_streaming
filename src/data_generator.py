import random
from datetime import datetime

class DataGenerator:
    @staticmethod
    def generate_sensor_data():
        return {
            'timestamp': datetime.now().isoformat(),
            'device_id': random.randint(1, 10),  # Explicitly include device_id
            'temperature': round(random.uniform(20, 35), 2),
            'humidity': round(random.uniform(30, 70), 2),
            'pressure': round(random.uniform(980, 1020), 2)
        }