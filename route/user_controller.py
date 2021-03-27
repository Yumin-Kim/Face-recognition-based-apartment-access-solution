from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
import model

User = Namespace("User")

@User.route("")
class UserRoute(Resource):
    def get(self):
        
        model.my_function()
        return jsonify({"data":"User"})