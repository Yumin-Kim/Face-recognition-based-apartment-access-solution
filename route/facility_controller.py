from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from route.user_controller import docBasicQueryString

Facility = Namespace("Facility")

@Facility.route("/toollog")
@Facility.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class FacilityToolResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Faciliity"})

@Facility.route("/toollog/toollist")
@Facility.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class FacilityToolListResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Faciliity"})

@Facility.route("/roomlog")
@Facility.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class FacilityRoomResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Faciliity"})

@Facility.route("/toollog/toollist")
@Facility.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class FacilityRoomListResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Faciliity"})