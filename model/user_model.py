from model import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def insert_userInfo():
    query = User(username = "Hello" , email="dbals0@naver.com")
    db.session.add(query)
    db.session.commit()
    return User.query.all()
