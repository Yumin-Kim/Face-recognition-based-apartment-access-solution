from database import create_app , User ,db
from flask_restx import Resource , Api , Namespace

from user import User 

app = create_app()
# app.app_context().push()
# db.create_all(app = create_app()) # 동적으로 table 생성 할 수 있는 코드 
api = Api(app)

api.add_namespace(User , "/user" )

@app.route("/")
def get():
	return str("HEllo")

if __name__ == "__main__":
	app.run(host="0.0.0.0",threaded=True , debug=True, port=5001)