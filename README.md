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

### Running via script

I also added a script that downloads and runs kafka. You can run like this:

- To downlaod and run:

``` shell
./download_and_run.sh dr
```

- Just run (If you have already downloaded):

``` shell
./download_and_run.sh
```

## Running Consumer and Producer

Before running the code, please install dependencies with:

```
pip install -r requirements.txt
```

It is really simple to run the producer and consumer. Just type:

```
python3 producer.py
```

In another terminal, run consumer.py:

```
python3 consumer.py
```
