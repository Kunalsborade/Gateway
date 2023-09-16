from app import app
from flask import request, jsonify 
from kafka import KafkaProducer
from pract import produce_responce
import json
import json
from consumer import consume_response

def get_payload(action, data):
    payload = {
        "action": action,
        "data": data
    }
    message = json.dumps(payload)
    return message


@app.route('/employee/register', methods = ['POST'])
def post():
    action = "Post"
    data = request.json
    payload = get_payload(action, data)
    produce_responce(payload)
    message = consume_response()
    return message
    
    

# @app.route('/employee/update/<int:id>', methods = ['PUT'])
# def put():
#     return("update")

# @app.route('/employee/all', methods = ['GET'])
# def getall():
#     return("employee all")

# @app.route('/employee/<int:id>', methods = ['GET'])
# def get():
#     return("register_1")

# @app.route('/employee/delete/<int:id>', methods = ['DELETE'])
# def delete():
#     return("delete")