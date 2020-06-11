from flask import Flask, render_template
from flask_restful import Api
from resources import user

app = Flask(__name__)
api = Api(app)

api.add_resource(user, '/api/user')

@app.route('/admin')
def adminView():
    return render_template("admin/admin.html", users=None)

@app.route('/admin/addUser')
def addUserView():
    return render_template("admin/addUser.html")
