from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from route.user_controller import docBasicQueryString

Petition = Namespace("Petition")

@Petition.route("")
@Petition.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ "kind" : "string : 시설 신고 기타" })
class PetitionsRoute(Resource):
    def get(self):
        return jsonify({"data":"Petition"})

# stage pathname과 비교하여 배열로 선언 ["접수" ,"서류 검토" , "검토 완료" , "처리중" , "처리완료"] 다음 값을 알아낼
# 해당 단계가 처리완료 단계 이면 수정이 안됨이라고 프론트에서 처리
# 해당 index가 검토완료의 index를 가지면 해당 row 테이블 에서 succesdAt현재 날짜를 수정해준다.
@Petition.route("/stage/<int:id>")
@Petition.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={"stage": "string : [접수 ,서류 검토 , 검토 완료 , 처리중 , 처리완료]"})
class PetitionsRoute(Resource):
    def get(self,id):
        return jsonify({"data":"Petition"})


