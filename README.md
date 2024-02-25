## Steps to use SDK

# 1)Clone the repository
git clone <repository-url>
cd <repository-directory>

# 2)Install Dependencies:
Ensure you have Python installed. Install the required dependencies using:
pip install -r requirements.txt

# 3)Initialize the SDK:
In your server application (example_server.py), initialize the TrafficSDK. You can do this by creating an instance of the TrafficSDK class and providing the required parameters (topic, limit, client_id, brokers).

from traffic_sdk.sdk import TrafficSDK, get_kafka_producer, send_to_kafka
sdk = TrafficSDK(topic='new-sdk', limit=10, client_id='example-producer', brokers='localhost:9092')

# 4)Integrate SDK in Server Routes:
In your server routes, use the SDK methods to process requests and responses.

@app.route('/api/test', methods=['POST'])
def test_endpoint():
    sdk.process_request(request)
    
    # Simulate some processing
    response_data = {'message': 'Request received successfully'}
    
    # Send a manual message to 'new-sdk' Kafka topic
    message_content = "Hi"
    manual_message = {
        'data': {
            'message_content': message_content,
            'additional_data': 'Any additional information you want to include',
        }
    }
    sdk.send_to_kafka([manual_message])
    
    return jsonify(response_data)

# 5)Run the Server:
Start your Flask server:
python example_server.py

# 6)Send Requests to Server:
Use a tool like cURL, Postman, or Invoke-RestMethod to send requests to your server's API endpoint.

Example using Invoke-RestMethod in PowerShell:
Invoke-RestMethod -Uri 'http://127.0.0.1:4000/api/test' -Method 'POST' -Body '{"key": "value"}' -Headers @{'Content-Type'='application/json'}

# 7)Check Console Logs:
As you send requests, observe the console logs of your server. You should see detailed print statements related to processing requests and sending messages to the Kafka topic.

# 8)Check Kafka Consumer:
Run a Kafka consumer to check if messages are being sent to the 'new-sdk' Kafka topic.

./bin/windows/kafka-console-consumer.bat --topic new-sdk --from-beginning --bootstrap-server localhost:9092

You should see the manually sent messages in the Kafka consumer.

# 9)Adjust for Production:
When deploying in production, make sure to configure the SDK and Kafka producer appropriately. Handle errors, secure credentials, and optimize for your production environment.

