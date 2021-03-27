from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

UserCar = Namespace("UserCar")

@UserCar.route("")
class UserCarRoute(Resource):
    def get(self):
        return jsonify({"data":"UserCar"})