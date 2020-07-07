# pylint: disable=no-value-for-parameter
from flask import Flask, render_template
from flask_restful import Api
from .resources.user import User
from .resources.authenticate import Authenticate
from .resources.image import Image
from .authenticated import authenticated, admin_authenticated
from database import users
import settings

app = Flask(__name__)
api = Api(app)

app.secret_key = settings.flask_secret_key

api.add_resource(User, '/api/users', '/api/users/<string:username>')
api.add_resource(Authenticate, '/api/authenticate')
api.add_resource(Image, '/api/images', '/api/images/<int:image_id>')

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

@app.route('/upload')
@authenticated
def upload():
    return render_template("upload.html")

@app.route('/gallery')
@authenticated
def gallery():
    return render_template("gallery.html")

@app.route('/admin')
@admin_authenticated
def adminView():
    return render_template("admin/admin.html", users=users.listUsers())

@app.route('/admin/user/<string:username>')
@admin_authenticated
def adminUserDetailsView(username):
    return render_template("admin/userDetails.html", user=users.getUser(username))

@app.route('/admin/addUser')
@admin_authenticated
def adminAddUserView():
    return render_template("admin/addUser.html")
