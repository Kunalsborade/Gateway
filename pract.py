from kafka import KafkaProducer

def produce_responce(message):
    topic = 'employee'  
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092' ,
        value_serializer=lambda v: str(v).encode('utf-8')  
    )
    producer.send(topic, value = message)
    producer.close()
