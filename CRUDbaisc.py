# #insert
# @app.route("/insert", methods=['POST'])
# def insert_table():
#     values = request.get_json()
#     data = values['data']
#     db_class = database.Database()
#     sql = "INSERT INTO test_table(test) VALUES('%s')" % (data)
#     db_class.execute(sql)
#     db_class.commit()

#     return jsonify(values), 200

# #select all
# @app.route("/select_all", methods=['GET'])
# def select_all():
#     db_class = database.Database()
#     sql = "SELECT * FROM users"
#     row = db_class.execute_all(sql)
#     print(row)
#     row = "" if not row else row
#     #조회후 데이터 반환시 함수를 통해서 반환되어야 하며 str() , jsonify() 를 사용하여 무조건 반환해줘야한다.
#     return str(row), 200 

# #select one
# def select_one(idx):
#     db_class = database.Database()
#     select_sql = "SELECT idx, test FROM test_table WHERE idx=('%s')" % (idx)
#     row = db_class.execute_one(select_sql)

#     row = "" if not row else row

#     return row

# #update
# @app.route("/update", methods=['POST'])
# def update_one():
#     '''
#     form에서 속성값을 받아올때
#     request.form.get("value)

#     form에서 속성값을 받은 후에 바로 dict로 변환할때
#     request.form.to_dict()
    
#     json으로 속성값을 바로 받아올때
#     request.get_json()
#     '''

#     values = request.get_json()
#     db_class = database.Database()
#     data = values['data']
#     idx = values['idx']
#     update_sql = "UPDATE test_table SET test=('%s') WHERE idx=('%r')" % (data, idx)
#     db_class.execute(update_sql)
#     db_class.commit()

#     # 방금 update한 row를 select 해온다.
#     # select 는 여러번 재사용 할 수 있기 때문에 메서드를 분리
#     row = select_one(idx)

#     return jsonify(row), 200

# #delete
# @app.route("/delete_one", methods=['POST'])
# def delete_one():
#     values = request.get_json()
#     db_class = database.Database()
#     idx = values['idx']

#     # data가 존재하는지 확인
#     row = select_one(idx)

#     # 없으면 pass
#     if not row:
#         pass
#     # 있다면 삭제를 수행한다
#     else:
#         delete_sql = "DELETE FROM test_table where idx=('%r')" % (idx)
#         db_class.execute(delete_sql)
#         db_class.commit()

#     return jsonify(""), 200







# @app.route("/",methods=["get", "pose"])
# def basicRoute():
#     return "Route File"
    
# @app.route("/hi", methods=["GET"])
# def hi():
#     return "hi"

# @app.route("/compare" , methods=["POST"])
# def compare_image():
#     if request.method == "POST":
#         result = "진행중"
#         if "file" not in request.files:
#             return "파일이 없습니다"
        
#         file = request.files["file"]

#         if file.filename == "":
#             return "이미지에 이름이 없습니다"
#         if file and allowed_file(file.filename):
#             return compare_image()

# @app.route("/admin")
# def 