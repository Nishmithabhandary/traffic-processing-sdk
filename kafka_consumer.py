from confluent_kafka import Consumer, KafkaError

# Define Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
}

# Create Kafka consumer
consumer = Consumer(consumer_conf)

# Subscribe to the 'new-sdk' topic
consumer.subscribe(['new-sdk'])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)  # Adjust the timeout as needed

        if msg is None:
            continue
        if msg.error():
            # Handle any errors
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Reached end of partition {msg.partition()}")
            else:
                print(f"Error: {msg.error()}")
        else:
            # Print the received message value
            print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
