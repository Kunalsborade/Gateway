from kafka import KafkaProducer
import atexit 

KAFKA_PRODUCER = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)

def produce_kafka_message(message):
    """
    Produces a message to the specified Kafka topic.
    :param topic: The Kafka topic to send the message to.
    :param message: The message to send.
    """
    topic = 'employee'
    KAFKA_PRODUCER.send(topic, value=message)

# Close the Kafka producer when the application exits
atexit.register(KAFKA_PRODUCER.close)
