from database import users
from flask import jsonify, request 
from flask_restful import Resource

class User(Resource):
    def get(self):
        return jsonify({'message': 'hello world'}) 
  
    # Corresponds to POST request 
    def post(self):
        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201