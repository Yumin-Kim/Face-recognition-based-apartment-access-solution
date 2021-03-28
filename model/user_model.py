# db query return to json  
from dataclasses import dataclass
from datetime import date

from model import db
from sqlalchemy import exc
import pandas as pd

@dataclass
class Users(db.Model):
    id:int
    name:str
    memberIndex:int
    host:bool
    craetedAt:date
    updatedAt:date
    deletedAt:date
    birth:date
    phoneNumber:str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    memberIndex = db.Column(db.String(120),  nullable=False)
    host = db.Column(db.Boolean,  nullable=False)
    craetedAt = db.Column(db.DateTime,  nullable=False)
    updatedAt = db.Column(db.DateTime,  nullable=True)
    deletedAt = db.Column(db.DateTime,  nullable=True)
    birth = db.Column(db.DateTime,  nullable=False)
    phoneNumber = db.Column(db.String(15),  nullable=False)


# https://lowelllll.github.io/til/2019/04/19/TIL-flask-sqlalchemy-orm/

# SET @COUNT = 0;
# UPDATE `user` SET `id`  = @COUNT:=@COUNT+1;
# ALTER TABLE `user` AUTO_INCREMENT=1;

def insert_userInfo():
    query = Users(username = "김유민" , email="asdasd@sdfsdfaver.com")
    # try : 
    db.session.add(query)
    db.session.commit()
    return Users.query.all()
    # except exc.IntegrityError:
        # print("Error")
        # db.session.rollback()
        

def delete_userInfo():
    query = Users(username = "Hellsdasdasdasdasdfsdfo" , email="dasdasdsdfsdfaasdasdasdver.com")
    try : 
        Users.query.filter_by(id=1).delete()
        return Users.query.all()
    except exc.IntegrityError:
        print("Error")
        db.session.rollback()
        return db.session.query(Users).all()

def setAutoIncrement_userInfo():
    try : 
        reset ="SET @COUNT = 0"
        prin = db.session.execute(reset)
        reset =  "UPDATE user SET id  = @COUNT:=@COUNT+1"
        prin = db.session.execute(reset)
        reset = "ALTER TABLE user AUTO_INCREMENT=1"
        prin = db.session.execute(reset)
        return Users.query.all()
    except exc.IntegrityError:
        print(exc.IntegrityError)
        db.session.rollback()
        return db.session.query(Users).all()