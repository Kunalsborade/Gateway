from app import app
from flask import request
from kafka import KafkaProducer
from pract import produce_responce

def get_payload(action, data):
    """
    Create a payload dictionary with action and data.

    Args:
        action (str): The action to be included in the payload.
        data (dict): The data to be included in the payload.

    Returns:
        dict: The payload dictionary.
    """
    payload = {
        "action": action,
        "data": data
    }
    return payload


@app.route('/employee/register', methods = ['POST'])
def post():
    action = "Post"
    data = request.json
    payload = get_payload(action, data)
    produce_responce(payload)
    return "done"
    
    

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