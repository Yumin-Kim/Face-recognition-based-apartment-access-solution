from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from werkzeug.utils import secure_filename
import threading
import config as database
import os
import faceRecognition

Face = Namespace("Face")
global threadFaceDdataetectEndcoding
threadFaceDdataetectEndcoding =[]
db_class = database.Database()

@Face.route("")
class FaceIndexRoute(Resource):
    def get(self):
        return jsonify({"data":"faceRecogntion Site"})

#동시에 앱을 사용할 수 있을때 해당학과의 인코딩 정보가 전송되지 않고 하나의 전역변수로 인해서 한학과로 타 학과의 학생을 판별하는 경우가 발생
# 위와 같은 문제를 해결하기 위해서 멀티스레드 등등 다른 방법들이 필요하다
# socketio
@Face.route("/encode/<string:groupName>")
class encodeClass(Resource):
    def get(self,groupName):
        if os.path.isdir("./static/images/%s"%groupName):
            files = os.listdir("./static/images/%s"%groupName)
            
            # threadFaceDdataetectEndcoding ([인코딩 정보<배열>],[이름<배열>],{"groupName" : groupName})
            if len(threadFaceDdataetectEndcoding) != 0:
                for a in range(len(threadFaceDdataetectEndcoding)) :
                    if threadFaceDdataetectEndcoding[a][2]["groupName"] != groupName: 
                        threadFaceDdataetectEndcoding.append(faceRecognition.encoding_images("./static/images/%s"%groupName,files,groupName))
                        resultData = "CheckIn  : " + groupName
                    else:
                        resultData = "Already Data : " + groupName
            else:
                threadFaceDdataetectEndcoding.append(faceRecognition.encoding_images("./static/images/%s"%groupName,files,groupName))
                resultData = "CheckIn"
            # for a in range(len(threadFaceDdataetectEndcoding)) :
            #     print(threadFaceDdataetectEndcoding[a][2]["groupName"])
            return jsonify({"data":resultData})
#/encode/compare?groupName={멀티미디어학과}
@Face.doc(params={'groupName': "멀티미디어학과"})
@Face.route("/encode/compare")
class encodeClass(Resource):
    def post(self):
        groupName = request.args.get("groupName")
        if len(threadFaceDdataetectEndcoding) != 0:
            for index in range(len(threadFaceDdataetectEndcoding)):
                    if threadFaceDdataetectEndcoding[index][2]["groupName"] == groupName:
                        file = request.files['image']
                        data = faceRecognition.faceDetect_image(file,threadFaceDdataetectEndcoding[index])
                        return jsonify(data)
        else:
            return redirect('/face/encode/%s'%groupName)