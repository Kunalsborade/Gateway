from app import app
from flask import request, jsonify
import json
from kafka import KafkaProducer
from producer import produce_kafka_message
from consumer import consume_response

def send_payload(action, data=None, id=None):
    payload = {
        "action": action,
        "data": data,
        "id": id
    }
    payload = json.dumps(payload)
    produce_kafka_message(payload)
    response = consume_response()
    return response

@app.route('/employee/register', methods=['POST'])
def post():
    action = "Post"
    data = request.json
    response = send_payload(action, data)
    return jsonify(response)

@app.route('/employee/update/<int:id>', methods=['PUT'])
def put(id):
    action = "Put"
    data = json.loads(request.data)
    response = send_payload(action, data, id)
    return jsonify(response)

@app.route('/employee/<int:id>', methods=['GET'])
def get(id):
    action = "Get"
    response = send_payload(action, id=id)
    return jsonify(response)

@app.route('/employee/', methods=['GET'])
def get_all():
    action = "Get_all"
    response = send_payload(action)
    return jsonify(response)

@app.route('/employee/delete/<int:id>', methods=['DELETE'])
def delete(id):
    action = "Delete"
    response = send_payload(action, id=id)
    return jsonify(response)