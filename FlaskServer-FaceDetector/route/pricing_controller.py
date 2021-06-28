from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from route.user_controller import docBasicQueryString

Pricing = Namespace("Pricing")

@Pricing.route("")
@Pricing.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class PricingRoute(Resource):
    def get(self):
        return jsonify({"data":"Pricing"})