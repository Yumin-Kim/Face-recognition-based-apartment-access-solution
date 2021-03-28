from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from route.user_controller import docBasicQueryString
UserCar = Namespace("UserCar")

@UserCar.route("")
@UserCar.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString)
class UserCarRoute(Resource):
    def get(self):
        return jsonify({"data":"UserCar"})

@UserCar.route("/filter")
@UserCar.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString | {"carCode":"string" , "createdAt":"stirng -> Date", "kind":"string" , "group":"string" , "groupByGroup":"string" , "user" : "string"})
class UserCarFilterRoute(Resource):
    def get(self):
        return jsonify({"data":"UserCar"})
        
@UserCar.route("/filter/multi")
@UserCar.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params=docBasicQueryString| {"carCode":"string" , "createdAt":"stirng -> Date", "kind":"string" , "group":"string" , "groupByGroup":"string" , "user" : "string"})
class UserCarMultiFilterRoute(Resource):
    def get(self):
        return jsonify({"data":"UserCar"})