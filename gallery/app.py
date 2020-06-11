# pylint: disable=no-value-for-parameter
from flask import Flask, render_template
from flask_restful import Api
from .resources.user import User
from database import users

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/api/users', '/api/users/<string:username>')

@app.route('/admin')
def adminView():
    return render_template("admin/admin.html", users=users.listUsers())

@app.route('/admin/user/<string:username>')
def adminUserDetailsView(username):
    return render_template("admin/userDetails.html", user=users.getUser(username))

@app.route('/admin/addUser')
def adminAddUserView():
    return render_template("admin/addUser.html")
