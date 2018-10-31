from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 consumer_timeout_ms=1000)
consumer.subscribe(['my-topic'])

while True:
    for message in consumer:
        print(message.value)