from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace

Voting = Namespace("Voting")

@Voting.route("")
class VotingRoute(Resource):
    def get(self):
        return jsonify({"data":"Voting"})