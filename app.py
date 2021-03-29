# 파이썬 폴더 모듈화 하는 방법 : 원하는 폴더 만들고 __init__.py 
# externals Library
from flask import render_template ,redirect ,Flask
from flask_restx import Resource , Api , Namespace

# Defined Module
# import faceRecognition
from route import User,Admin,Registering,Voting,Petition,Facility,Pricing,UserCar
from model import db

from model.user_model import Users , Groups ,GroupByGroups ,AccessMembers
from model.admin_model import Admins,Days,Admindashboards,admin_day_mapping
from model.facility_model import FacilityInfos,FacilityRoomLists,FacilityToolLists,facility_List_mapping
from model.outter_model import OutterUsers
from model.image_model import user_image_mapping , ImageOutters , Images , outteruser_image_mapping
from model.petitions_model import Petitions
from model.pricing_model import PricingInfos
from model.voting_model import VotingInfos

# app = Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:wjqrmsrma!wl6311@localhost:3306/facerecognition?charset=utf8"
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4' # utf-8 인코딩


db.init_app(app)
app.app_context().push()
db.create_all(app=app)

# table 만드는 코드 서버 로딩하는 코드 분리하기
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
api.add_namespace(Petition , "/api/petition" )
api.add_namespace(Facility , "/api/facility" )
api.add_namespace(Pricing , "/api/pricing" )
api.add_namespace(UserCar , "/api/usercar" )

# 얼굴 인식 API
# api.add_namespace(Face , "/api/face" )

if __name__ == "__main__":
    app.run(host="0.0.0.0",threaded=True , debug=True, port=5001)