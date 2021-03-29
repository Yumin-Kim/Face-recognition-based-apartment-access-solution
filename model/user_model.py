# db query return to json  
from dataclasses import dataclass
from datetime import date

from model import db
from sqlalchemy import exc

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

@dataclass
class Group(db.Model):
    id:int
    name:int
    minWeight:int
    maxWeight:int
    createdAt:date
    updatedAt:date
    roomCount:int
    pricing:int

    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.Integer,  nullable=True),
    minWeight = db.Column(db.Integer,  nullable=True),
    maxWeight = db.Column(db.Integer,  nullable=True),
    createdAt = db.Column(db.DateTime,  nullable=True),
    updatedAt = db.Column(db.DateTime,  nullable=False),
    roomCount = db.Column(db.DateTime,  nullable=True),
    pricing = db.Column(db.Integer,  nullable=False),

@dataclass
class GroupByGroup(db.Model):
    id : int
    name: int 
    repairCount:int
    createdAt:date
    updatedAt:date
    deletedAt:date
    housePassword:str
    pricing:int
    
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.Integer,  nullable=False),
    repairCount = db.Column(db.Integer,  nullable=False),
    createdAt = db.Column(db.DateTime,  nullable=False),
    updatedAt = db.Column(db.DateTime,  nullable=True),
    deletedAt = db.Column(db.DateTime,  nullable=True),
    roomCount = db.Column(db.DateTime,  nullable=False),
    housePassword = db.Column(db.Integer,  nullable=False),
    pricing = db.Column(db.Integer,  nullable=False),

# 1대 다 관계 정의 필요
@dataclass
class AccessMember(db.Model):
    id:int
    admisssionTime:date

    id = db.Column(db.Integer,primary_key=True),
    admisssionTime = db.Column(db.Integer,nullable=False)
    

# https://lowelllll.github.io/til/2019/04/19/TIL-flask-sqlalchemy-orm/

# SET @COUNT = 0;
# UPDATE `user` SET `id`  = @COUNT:=@COUNT+1;
# ALTER TABLE `user` AUTO_INCREMENT=1;

def insert_userInfo():
    query = Users(name = "김유민" , memberIndex="asdasd@sdfsdfaver.com")
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