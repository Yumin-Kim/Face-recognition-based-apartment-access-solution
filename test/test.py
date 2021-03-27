from flask import Flask, render_template , jsonify
from flask_sqlalchemy import SQLAlchemy
from model import Members

app = Flask(__name__)

# database 설정파일
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:wjqrmsrma!wl6311@localhost:3306/facerecognition"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

    
@app.route("/one")
def home():
	member = Members.query.first()
	return 'Hello {0}, {1}, {2}, {3}, {4}'\
		.format(member.name, member.email, member.phone, member.start.isoformat(), member.end.isoformat())
	#return render_template('home.html')
    
@app.route('/all')
def select_all():
    members = Members.query.all()
    return str(members[0].email)

if(__name__ == "__main__"):
	app.run(host="0.0.0.0",threaded=True , debug=True, port=5001)