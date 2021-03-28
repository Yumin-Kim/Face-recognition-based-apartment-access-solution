# Python에서 제공하는 ORM을 통해서 프로그램을 진행할 예정
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:wjqrmsrma!wl6311@localhost:3306/facerecognition"
    from model.user_model import User
    db.init_app(app)
    return app



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
