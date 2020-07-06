# pylint: disable=no-value-for-parameter
from database import users
from flask import jsonify, request, session
from flask_restful import Resource

class Authenticate(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        if users.userIsAuthenticated(username, password):
            session['username'] = username
            return "User Authenticated", 200
        else:
            return "Error: Wrong Username or Password", 401