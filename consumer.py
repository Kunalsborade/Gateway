from kafka import KafkaConsumer

topic = 'employee_reply'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers='localhost:9092',  
    auto_offset_reset='latest',  
    enable_auto_commit=True,  
    auto_commit_interval_ms=1000,  
    value_deserializer=lambda x: x.decode('utf-8') 
    )
consumer.subscribe(topics=topic)

def consume_response():
    for message in consumer:
        res = message.value
        return res
        
   
