# traffic_sdk/sdk.py
from kafka import KafkaProducer

class TrafficSDK:
    def __init__(self, topic, limit, client_id, brokers):
        self.topic = topic
        self.limit = limit
        self.client_id = client_id
        self.brokers = brokers

    def process_request(self, request):
        # Log request details or perform any necessary processing
        print(f"Processing Request: {request.method} {request.url}")

    def process_response(self, response):
        # Log response details or perform any necessary processing
        print(f"Processing Response: {response.status_code}")

    def send_to_kafka(self, messages):
        # Initialize Kafka producer
        producer = KafkaProducer(bootstrap_servers=self.brokers, client_id=self.client_id)

        # Send messages to Kafka topic
        try:
            for message in messages:
                value = message['data']['message_content'].encode('utf-8')
                print(f"Sending message to Kafka topic '{self.topic}': {value}")
                producer.send(self.topic, value=value)
        except Exception as e:
            print(f"Error sending message to Kafka: {e}")
            # Print the full exception details
            import traceback
            traceback.print_exc()
        finally:
            producer.close()
