# pylint: disable=no-value-for-parameter
from database import images
from flask import jsonify, request, session
from flask_restful import Resource
from ..authenticated import authenticated

class Image(Resource):
    @authenticated
    def get(self, image_id=None):
        username = session['username']
        if image_id is None:
            return jsonify(images.listImages(username))
        else:
            image = images.getImage(username, image_id)
            if image is None:
                return f"Error: An image with the id {image_id} could not be found under username {username}", 404
            else:
                return jsonify(image)

    @authenticated
    def post(self):
        username = session['username']
        # upload to s3
        return "Image uploaded successfully", 201

    @authenticated
    def delete(self, image_id):
        username = session['username']
        if images.imageExists(username, image_id):
            images.deleteImage(username, image_id)
            return "Image successfully deleted", 200
        else:
            return f"Error: An image with the id {image_id} could not be found under username {username}", 404