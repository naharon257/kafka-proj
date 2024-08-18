from confluent_kafka import Producer
import sys
import time
from datetime import datetime


# Define the Kafka producer configuration
conf = {
    'bootstrap.servers': 'broker-1:9092,broker-2:9093,broker-3:9094'
}

# Create a Kafka producer instance
producer = Producer(conf)


def delivery_report(err, msg):
    """Delivery report callback function."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def main():

    counter = 0

    while True:
        try:
            counter += 1
            message = f"hey{counter}"
            # Produce the message
            now = datetime.now()
            producer.produce("first_topic", message, callback=delivery_report)
            producer.flush()
            print(f"Produced message: {message} Time: {now}")
            time.sleep(10)

        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break

    # Clean up any remaining messages in the producer's queue
    producer.flush()

if __name__ == "__main__":
    main()
