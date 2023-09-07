from kafka import KafkaProducer

def produce_responce(message):
    topic = 'employee'  
    # Create a KafkaProducer instance
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092' ,
        value_serializer=lambda v: str(v).encode('utf-8')  
    )
    # Send a message to the Kafka topic
    producer.send(topic, value = message)
    producer.close()
