from dataclasses import dataclass
from datetime import date

from model import db


@dataclass
class UserCarInfos(db.Model):
    id:int
    kind:str
    carCode:str
    createdAt:date
    updatedAt:date
    deletedAt:date
    user_id:int
    group_id:int
    groupBy_id:int

    id = db.Column(db.Integer , primary_key=True)
    kind = db.Column(db.String(10),nullable=False)
    carCode = db.Column(db.String(20),nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)

@dataclass
class ParkingInfos(db.Model):
    id:int
    space:str
    valid:bool
    startTime:date
    EndTime:date
    specificSpace:bool
    user_id:int
    group_id:int
    groupBy_id:int
    userCarInfo_id:int

    id = db.Column(db.Integer , primary_key=True)
    space = db.Column(db.String(20),nullable=False)
    valid = db.Column(db.Boolean,nullable=False)
    startTime = db.Column(db.DateTime,nullable=False)
    EndTime = db.Column(db.DateTime,nullable=False)
    specificSpace = db.Column(db.Boolean,nullable=False)
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)
    userCarInfo_id = db.Column(db.Integer , db.ForeignKey("user_car_infos.id"),nullable=False)
