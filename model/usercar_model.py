from dataclasses import dataclass
from datetime import date

from model import db


@dataclass
class UserCarInfo(db.Model):
    id:int
    kind:str
    carCode:str
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    kind = db.Column(db.String(10),nullable=False)
    carCode = db.Column(db.String(20),nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)

@dataclass
class ParkingInfo(db.Model):
    id:int
    space:str
    valid:bool
    startTime:date
    EndTime:date
    specificSpace:bool

    id = db.Column(db.Integer , primary_key=True)
    space = db.Column(db.String(20),nullable=False)
    valid = db.Column(db.Boolean,nullable=False)
    startTime = db.Column(db.DateTime,nullable=False)
    EndTime = db.Column(db.DateTime,nullable=False)
    specificSpace = db.Column(db.Boolean,nullable=False)
