# pylint: disable=no-value-for-parameter
from database import users
from flask import jsonify, request 
from flask_restful import Resource
from ..authenticated import admin_authenticated

class User(Resource):
    @admin_authenticated
    def get(self, username=None):
        if username is None:
            return jsonify(users.listUsers())
        else:
            user = users.getUser(username)
            if user is None:
                return f"Error: A user with the username {username} could not be found", 404
            else:
                return jsonify(user)
    
    @admin_authenticated
    def post(self):
        username = request.form['username']
        password = request.form['password']
        fullName = request.form['fullName']
        if users.userExists(username):
            return f"Error: A user with the username {username} already exists", 409, {'Location': '/api/users/' + username}
        else:
            users.addUser(username, password, fullName)
            return "User created successfully", 201
    
    @admin_authenticated
    def put(self, username=None):
        if username is None:
            return "Error: A user was not specified", 404

        password = request.form['password']
        fullName = request.form['fullName']
        if users.userExists(username):
            users.updateUser(username, password, fullName)
            return f"Successfully updated user {username}", 200
        else:
            return f"Error: A user with the username {username} could not be found", 404

    @admin_authenticated
    def delete(self, username=None):
        if username is None:
            return "Error: A user was not specified", 404
        
        if users.userExists(username):
            users.deleteUser(username)
            return f"Successfully deleted user {username}", 200
        else:
            return f"Error: A user with the username {username} could not be found", 404