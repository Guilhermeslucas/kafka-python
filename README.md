# kafka-python

This is the absolutely beginner code for inserting messages and consuming them at a kakfa.  
I'm running it using a local kafka cluster, just to study the API's and some core concepts from Kafka.

## Running Kafka locally

Running a kafka cluster locally is a extremely straighforward. You just have to 
download the binaries and start Zookeper and Kakfa itself.

To get the files needed for Kakfka and Zookeper, download a version of the binary
on this [link](https://www.apache.org/dyn/closer.cgi?path=/kafka/1.0.0/kafka_2.11-1.0.0.tgz) you also need Java installed.

Then extract the components inside this folder with this command:

```
tar -xzvf kafka_2.11-1.0.0.tgz

```

Now go inside the folder you had just unpacked and open two terminals.

### Running Zookeper

On the first terminal, run:

```

bin/zookeeper-server-start.sh config/zookeeper.properties

```

Now, you have Zookeper running.

### Running Kafka

On the second terminal, run:

```
bin/kafka-server-start.sh config/server.properties

```

Done. Now you have a local Kafka running on ```localhost:9092```.