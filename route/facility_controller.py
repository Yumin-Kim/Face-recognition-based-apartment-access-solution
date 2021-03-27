from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Facility = Namespace("Facility")

@Facility.route("")
class FacilityRoute(Resource):
    def get(self):
        return jsonify({"data":"Faciliity"})