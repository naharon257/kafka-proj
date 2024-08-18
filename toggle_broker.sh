#!/bin/bash

# List of broker container names
brokers=("broker-1" "broker-2" "broker-3")

while true; do

  # Select a random broker
  random_broker=${brokers[$RANDOM % ${#brokers[@]}]}

  echo "Stopping $random_broker..."
  docker-compose -f zk-single-kafka-multiple.yml stop $random_broker

  sleep 30  # Wait for 10 seconds

  echo "Starting $random_broker..."
  docker-compose -f zk-single-kafka-multiple.yml start $random_broker

done
