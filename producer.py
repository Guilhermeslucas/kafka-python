from kafka import KafkaConsumer, KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    for i in range(0,10):
        message = "TESTING KAKFA : {}".format(i)
        producer.send('my-topic', bytes(message ,encoding='utf8'))
