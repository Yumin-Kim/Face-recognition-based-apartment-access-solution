from dataclasses import dataclass
from datetime import date

from model import db
#1대다관계 정의
@dataclass
class OutterUser(db.Model):
    id:int
    name:str
    description:str
    createdAt:date
    updatedAt:date
    phoneNumber:str

    id = db.Column(db.Integer,primary_key=True),
    name = db.Column(db.String(80),nullable=False),
    description = db.Column(db.String(300),nullable=False),
    createdAt = db.Column(db.DateTime,nullable=False),
    updatedAt = db.Column(db.DateTime,nullable=True),
    phoneNumber = db.Column(db.String(30),nullable=False),
