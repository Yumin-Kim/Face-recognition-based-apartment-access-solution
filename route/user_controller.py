from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from model.user_model import insert_userInfo

User = Namespace("User")

@User.route("")
class UserRoute(Resource):
    def get(self):
        data = insert_userInfo()
        print(data)
        return jsonify({"data":"User"})