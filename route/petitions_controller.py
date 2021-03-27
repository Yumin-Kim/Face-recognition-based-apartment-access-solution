from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Petitions = Namespace("Petitions")

@Petitions.route("")
class PetitionsRoute(Resource):
    def get(self):
        return jsonify({"data":"Petitions"})