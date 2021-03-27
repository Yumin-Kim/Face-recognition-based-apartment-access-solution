from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Admin = Namespace("Admin")
import model

@Admin.route("")
class AdminRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})