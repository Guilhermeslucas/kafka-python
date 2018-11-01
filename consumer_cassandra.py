from kafka import KafkaConsumer, KafkaProducer
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('messages')
session.execute("""
        CREATE KEYSPACE IF NOT EXISTS messages 
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
        """ )

session.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            message text,
            PRIMARY KEY (message)
        )
        """)

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 consumer_timeout_ms=1000)
consumer.subscribe(['my-topic'])

while True:
    for message in consumer:
        print(message.value)
        session.execute('INSERT INTO messages (message) VALUES (%s)', (str(message.value),))
