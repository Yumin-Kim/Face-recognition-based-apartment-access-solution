from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Registering = Namespace("Registering")

@Registering.route("")
class RegisteringRoute(Resource):
    def get(self):
        return jsonify({"data":"Registering"})

#formdata를 통해서 로직 구성.
#사진 upload로직 구성 필요
@Registering.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Registering.route("/registering/inner")
class InnerRegisteringRoute(Resource):
    def post(self):
        return jsonify({"data":"Registering"})

#formdata를 통해서 로직 구성.
#사진 upload로직 구성 필요
@Registering.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Registering.route("/registering/outter")
class OutterRegisteringRoute(Resource):
    def post(self):
        return jsonify({"data":"Registering"})
