#!/bin/bash

if [ "$1" == "dr" ]; then
    # Downloads kafka and zookeper binaries
    wget https://archive.apache.org/dist/kafka/1.1.0/kafka_2.11-1.1.0.tgz
    tar -xzvf kafka_2.11-1.1.0.tgz
fi

cd kafka_2.11-1.1.0

bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties