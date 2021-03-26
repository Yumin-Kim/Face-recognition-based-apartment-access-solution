from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from database import Users , db
from database_admin import Admin , Admin_user
User = Namespace("User")

@User.route("")
class UserIndexRoute(Resource):
    def get(self):
        # query = Users(username = "Hello" , email="dbals0@naver.com")
        # db.session.add(query)
        # db.session.commit()
        data=Users.query.all()
        print(data)
        return jsonify({"data":"asd"})

@User.route("/test")
class AdminIndexRoute(Resource):
    def get(self):
        return jsonify({"admin":"UserRecogntion Site"})

