# traffic_sdk/example_server.py
from flask import Flask, request, jsonify
from traffic_sdk.sdk import TrafficSDK

app = Flask(__name__)

# Initialize the SDK
sdk = TrafficSDK(topic='new-sdk', limit=10, client_id='example-producer', brokers='localhost:9092')

@app.route('/')
def index():
    return 'Hello, this is the example server!'

@app.route('/api/test', methods=['POST'])
def test_endpoint():
    sdk.process_request(request)
    
    # Simulate some processing
    response_data = {'message': 'Request received successfully'}
    
    # Send a manual message to 'new-sdk' Kafka topic
    message_content = "New sdk creation"
    manual_message = {
        'data': {
            'message_content': message_content,
            'additional_data': 'Any additional information you want to include',
        }
    }
    sdk.send_to_kafka([manual_message])
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
