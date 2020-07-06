# pylint: disable=no-value-for-parameter
from flask import Flask, render_template
from flask_restful import Api
from .resources.user import User
from .resources.authenticate import Authenticate
from .authenticated import authenticated
from database import users
import settings

app = Flask(__name__)
api = Api(app)

app.secret_key = settings.flask_secret_key

api.add_resource(User, '/api/users', '/api/users/<string:username>')
api.add_resource(Authenticate, '/api/authenticate')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/home')
@authenticated
def home():
    return render_template("home.html")

@app.route('/admin')
def adminView():
    return render_template("admin/admin.html", users=users.listUsers())

@app.route('/admin/user/<string:username>')
def adminUserDetailsView(username):
    return render_template("admin/userDetails.html", user=users.getUser(username))

@app.route('/admin/addUser')
def adminAddUserView():
    return render_template("admin/addUser.html")
