from confluent_kafka import Consumer, KafkaError
import sys
from datetime import datetime

def main():
    # Define the Kafka consumer configuration
    conf = {
        'bootstrap.servers': 'broker-1:9092,broker-2:9093,broker-3:9094',
        'group.id': 'consumer-group',
        'auto.offset.reset': 'earliest'
    }

    # Create a Kafka consumer instance
    consumer = Consumer(conf)

    topic = "second_topic"
    # Subscribe to the specified topic
    consumer.subscribe([topic])

    print(f"Consuming messages from topic: {topic}")

    try:
        # Continuously consume messages
        while True:
            now = datetime.now()
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break
            print(f"Consumed message: {msg.value().decode('utf-8')} Time: {now}")

    except KeyboardInterrupt:
        print("\nInterrupted by user")

    finally:
        # Close the consumer
        consumer.close()

if __name__ == "__main__":
    main()
