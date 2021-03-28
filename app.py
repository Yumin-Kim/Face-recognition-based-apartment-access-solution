# 파이썬 폴더 모듈화 하는 방법 : 원하는 폴더 만들고 __init__.py 
# externals Library
from flask import render_template ,redirect
from flask_restx import Resource , Api , Namespace

# Defined Module
# import faceRecognition
from route import User,Admin,Registering,Voting,Petitions,Facility,Pricing,UserCar
from model import create_app , db
app = create_app()
db.create_all(app=create_app())

#React[SPA]를 위한 Route >> Routing 되기전에 미리 Basic Route 선점
@app.route("/")
def get():
	return render_template("index.html")

# 아래 코드로 인해서 Swagger 문서작성 및 라우팅까지 가능
api = Api(app,
    title='얼굴 인식을 통한 아파트 출입관리 페이지 작성 03.25',
    version='v0.1',
    doc='/documentation')

#Convert JSON data utg-8  
app.config["JSON_AS_ASCII"] = False


# routing
api.add_namespace(User , "/api/user" )
api.add_namespace(Admin , "/api/admin" )
api.add_namespace(Registering , "/api/registering" )
api.add_namespace(Voting , "/api/voting" )
api.add_namespace(Petitions , "/api/petitions" )
api.add_namespace(Facility , "/api/facility" )
api.add_namespace(Pricing , "/api/pricing" )
api.add_namespace(UserCar , "/api/usercar" )


# 얼굴 인식 API
# api.add_namespace(Face , "/api/face" )

if __name__ == "__main__":
	app.run(host="0.0.0.0",threaded=True , debug=True, port=5001)