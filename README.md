Sure, here's a concise README for the Kafka streaming demo and visualization with PowerBI:

## Kafka Streaming Demo with PowerBI

This project demonstrates a simple Kafka streaming pipeline, integrating with a PostgreSQL database and visualizing the data in PowerBI.

### Architecture

The architecture consists of the following components:

1. **Producer**: Python script that generates sample sensor data and publishes it to a Kafka topic.
2. **Kafka**: The distributed streaming platform that receives and routes the data.
3. **Consumer**: Python script that consumes the data from the Kafka topic, processes it, and stores it in a PostgreSQL database.
4. **PostgreSQL**: The database that stores the processed sensor data.
5. **PowerBI**: The business intelligence tool used to visualize the data in real-time.

### Prerequisites

- Docker and Docker Compose
- Python 3.x with `pip`

### Setup

1. **Docker Images**:
   ```bash
   docker pull postgres:latest
   docker pull confluentinc/cp-zookeeper:latest
   docker pull confluentinc/cp-kafka:latest
   ```

2. **Docker Compose**:
   ```bash
   docker-compose up
   ```
   This will start the Kafka, Zookeeper, and PostgreSQL containers.

3. **Python Scripts**:
   - `src/producer.py`: Runs the data producer, publishing to the Kafka topic.
   - `src/consumer.py`: Runs the consumer, consuming from the Kafka topic and storing data in PostgreSQL.
   
   Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **PowerBI Configuration**:
   - Open PowerBI Desktop
   - Connect to the PostgreSQL database
   - Create visualizations using the `sensor_data` table

### Running the Demo

1. Start the Kafka producer:
   ```bash
   python src/producer.py
   ```
   This will continuously generate and publish sensor data to the Kafka topic.

2. Start the Kafka consumer:
   ```bash
   python src/consumer.py
   ```
   This will consume the data from the Kafka topic and store it in the PostgreSQL database.

3. In PowerBI, the `sensor_data` table should start populating, allowing you to build real-time visualizations.

### Verification

- Check the Kafka topic for messages:
  ```bash
  docker exec -it kafka_container kafka-console-consumer --bootstrap-server localhost:9092 --topic sensor_data
  ```
- Verify the PostgreSQL data:
  ```bash
  docker exec -it postgres_container psql -U your_username -d your_database
  > SELECT * FROM sensor_data LIMIT 10;
  ```