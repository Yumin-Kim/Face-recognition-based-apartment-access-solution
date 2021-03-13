from flask import request , jsonify , render_template , make_response , redirect
from flask_restx import Resource, Api, Namespace
from werkzeug.utils import secure_filename
import config as database
import os
Admin = Namespace("admin")

db_class = database.Database()
data = ""
# DB 조회 필요
# 파일명 수정 및 폴더 생성 코드
# os.mkdir("./static/%d" %group_id)
# f.filename = "test.jpg"
# 폴더 유무 체크
# os.path.isdir("./static/%d" %group_id)


def FindMiddlewareGroupFolder():
    sql = "SELECT * from groups"
    rows = db_class.execute_all(sql)
    for row in rows:
        if os.path.isdir("./static/images/%s" %row["name"]):
            print("존재하는 Group폴더입니다")
        else:
            os.mkdir("./static/images/%s" %row["name"])


@Admin.route('')
class TodoPost(Resource):
    def get(self):
        sql = "SELECT * FROM users"
        row = db_class.execute_all(sql)
        print(row)
        return jsonify(row)
        
@Admin.route("/image/")
class UploadHTML(Resource):
    def get(self):
        FindMiddlewareGroupFolder()
        # html rendering위해서 header안에 Content-Type안에 text/html을 집어 넣어준다
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("upload.html"),200,headers)

#이미지 저장 path 보다는 querystring으로 db조회및 저장
@Admin.route("/image/upload")
class UploadPost(Resource):
    def post(self):
        if request.method == "POST":
            teacherId = request.args.get("teacher")
            groupId = int(request.args.get("group"))
            userCode = request.args.get("userCode")
            if 'file' not in request.files:
                return jsonify({
                    data:"이미지 확인해주세요"
                })
            f = request.files["file"]

            findUserGroup = "SElECT name from groups where id =('%d')"%groupId 
            groupName = db_class.executeOneTryCatch(findUserGroup , "없는과입니다" )

            findUsersql = "SElECT userCode , id from users where userCode =('%s')"%userCode
            userData = db_class.executeOneTryCatch(findUsersql , "없는 힉생입니다" )
            if  True in userData : 
                requestGetUserImages = "select name from images where name = ('%d')"%userData[1]["userCode"]
                imageData = db_class.executeOneTryCatch(requestGetUserImages,1)

                if True in imageData :
                    imageLength = len(imageData[1]) + 1 
                    update_sql = "UPDATE images SET imageIndex=('%d') WHERE name=('%d')" % (imageLength, int(userData[1]["userCode"]))
                    db_class.execute(update_sql)
                    db_class.commit()
                else :
                    imageLength = imageData["data"]
                    sql = "INSERT INTO images(name , userId , teacherId , imageIndex ) VALUES( %d , %d , %d ,%d  )" % (int(userData[1]["userCode"]) , userData[1]["id"] ,int(teacherId) ,imageLength )
                    db_class.execute(sql)
                    db_class.commit()
                    
                f.filename = str(userData[1]["userCode"])+ "_"+ str(imageLength)+".jpg"
                f.save("./static/images/%s/" %groupName[1]["name"] +secure_filename(f.filename))
                
                return jsonify({
                    data:"성공적으로 이미지가 저장되었습니다"
                    }) 
            else :
                return jsonify(userData)
            