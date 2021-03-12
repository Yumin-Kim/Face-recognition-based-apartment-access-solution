# 파이썬 폴더 모듈화 하는 방법 : 원하는 폴더 만들고 __init__.py 
# externals Library
from flask import Flask
from flask_restx import Resource , Api
# import math
# import numpy as np

# Defined Module
import faceRecognition
from route import Todo , Admin
app = Flask(__name__)

# 아래 코드로 인해서 Swagger 문서작성 및 라우팅까지 가능
api = Api(app,title="FaceRecognition admin Page",terms_url="/api")

#Convert JSON data utg-8  
app.config["JSON_AS_ASCII"] = False

# routing
api.add_namespace(Todo , "/todos" )
# api.add_namespace(Admin , "/face" )
api.add_namespace(Admin , "/admin" )
# api.add_namespace(Todo , "/user" )


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5001)