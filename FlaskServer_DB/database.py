from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#https://stackoverflow.com/questions/22252397/importerror-no-module-named-mysqldb
# Mysql + pymysql 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{비밀번호 입력}@localhost:3306/test"
    db.init_app(app)
    return app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# app = Flask(__name__)


