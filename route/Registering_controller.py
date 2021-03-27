from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Registering = Namespace("Registering")

@Registering.route("")
class RegisteringRoute(Resource):
    def get(self):
        return jsonify({"data":"Registering"})