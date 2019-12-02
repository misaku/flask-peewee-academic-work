from App.Model.UserAuth import * 
from flask import jsonify
from flask_restful import Resource
class Auth(Resource):
    def get(self):
        user = UserAuth.select()
        return jsonify(user)
