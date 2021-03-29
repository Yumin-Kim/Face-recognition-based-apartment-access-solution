from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from model.admin_model import insert_adminInfo

Admin = Namespace("Admin")

@Admin.route("")
class AdminRoute(Resource):
    def get(self):
        insert_adminInfo()
        return jsonify(insert_adminInfo())

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Admin.route("/dashboard")
class AdminDashboardRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})
    def post(self):
        return jsonify({"data":"Admin"})
    # formdata에 따라서 처리
    def patch(self):
        return jsonify({"data":"Admin"})

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={"offset":"int : 설정값을 통해서 삭제후 다음 rowr값 전달  "})
@Admin.route("/dashboard/<int:id>")
class AdminDashboardDeleteRoute(Resource):
    def delete(self,id):
        return jsonify({"data":"Admin"})

#formdata를 통해서 로직 구성.
@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Admin.route("/signup")
class AdminSignupRoute(Resource):
    def post(self):
        return jsonify({"data":"Admin"})

#formdata를 통해서 로직 구성.
@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Admin.route("/login")
class AdminLoginRoute(Resource):
    def post(self):
        return jsonify({"data":"Admin"})

#formdata를 통해서 로직 구성.
@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Admin.route("/logout")
class AdminLogoutRoute(Resource):
    def post(self):
        return jsonify({"data":"Admin"})

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			params={"group":"int : 몇동의 인원조회를 원하는지 기록"} )
@Admin.route("/chart/user")
class AdminUserChartRearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			params={"group":"int : 몇동의 인원조회를 원하는지 기록"} )
@Admin.route("/chart/parking")
class AdminParkingChartRearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			params={"group":"int : 몇동의 인원조회를 원하는지 기록"} )
@Admin.route("/chart/parking")
class AdminExitingUserChartRearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})

@Admin.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 )
@Admin.route("/chart/totalCount")
class AdminExitingUserChartRearchRoute(Resource):
    def get(self):
        return jsonify({"data":"Admin"})

