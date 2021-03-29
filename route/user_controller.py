from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from model.user_model import insert_userInfo , delete_userInfo , setAutoIncrement_userInfo
import json

User = Namespace("User")
# querystring은 doc paramas에 기록 pathname:
docBasicQueryString = { 'offset': '지정된 값으로 부터 limit값을 가지고 온다','limit': '지정된 값을 부터 얼마만큼의 row을 가지고 올지' }
userSearchQueryString = { "host":"boolean : 세대주" , "memeberIndex":"int : 가족구성원수" , "phoneNumber" : "string : 폰번호"  }
userGroupSearchString = {"minWeight":"int : 최소 면적 ","name":"int : 동","pricing": "int","roomCount":"int"}
userGroupByGroupSearchString = {"name":"int","createdAt":"Date","pricing":"int","offset":"int", "limit":"int"}
basicReturn = {"test" : "준비중입니다"}
@User.route("")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
class UserRoute(Resource):
    # test Code
    def get(self):
        data = insert_userInfo()
        return jsonify(test=data)
    # def delete(self):
    #     data = delete_userInfo()
    #     return jsonify(test=data)
    def patch(self):
        data = setAutoIncrement_userInfo()
        return jsonify(test=data)

@User.route("/filter/human")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			  )
class UserResearchRoute(Resource):
    def get(self):
        return jsonify(basicReturn)

@User.route("/filter/room/<string:tableName>")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			  )
class UserGroupResearchRoute(Resource):
    def get(self,tableName):
        return jsonify(basicReturn)

@User.route("/filter/info/<string:tableName_1>/<string:tableName_2>")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			  )
class MultiUserGroupResearchRoute(Resource):
    def get(self,tableName_1,tableName_2):
        return jsonify(basicReturn)

#form data를 통해서 정보 조회
@User.route("/changed/<int:id>")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 body=userSearchQueryString)
class UserUpdateRoute(Resource):
    def patch(self,id):
        return jsonify(basicReturn)

@User.route("/deleted")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
class UserDeleteRoute(Resource):
    def delete(self):
        return jsonify(basicReturn)

@User.route("/outter")
@User.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
class OutterUserResearchRoute(Resource):
    def get(self):
        return jsonify(basicReturn)

