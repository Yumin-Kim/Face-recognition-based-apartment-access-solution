from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from route.user_controller import docBasicQueryString

Voting = Namespace("Voting")

#formData를 통해서 로직 구성
@Voting.route("/registered")
@Voting.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
class VotingRegisterRoute(Resource):
    def post(self):
        return jsonify({"data":"Voting"})

@Voting.route("/progress")
@Voting.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }
,params=docBasicQueryString)
class VotingProgressResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Voting"})

@Voting.route("/deadline")
@Voting.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }
,params=docBasicQueryString)
class VotingDeadlineResearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Voting"})



