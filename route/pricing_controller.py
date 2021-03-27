from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Pricing = Namespace("Pricing")

@Pricing.route("")
class PricingRoute(Resource):
    def get(self):
        return jsonify({"data":"Pricing"})