# pylint: disable=no-value-for-parameter
from database import users
from flask import jsonify, request, session
from flask_restful import Resource

class Authenticate(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        authentication = users.userIsAuthenticated(username, password)
        if authentication[0]:
            session['username'] = username
            session['isAdmin'] = authentication[1]
            return "User Authenticated", 200
        else:
            return "Error: Wrong Username or Password", 401