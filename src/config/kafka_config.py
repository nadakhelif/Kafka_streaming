KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT'
}

PRODUCER_CONFIG = {
    **KAFKA_CONFIG,
    'client.id': 'demo-producer'
}

CONSUMER_CONFIG = {
    **KAFKA_CONFIG,
    'group.id': 'demo-consumer-group',
    'auto.offset.reset': 'earliest'
}
