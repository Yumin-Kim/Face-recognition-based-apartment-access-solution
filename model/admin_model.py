from dataclasses import dataclass
from datetime import date

from model import db
from sqlalchemy import exc

admin_day = db.Table("admin_day",
    db.Column("admins_id",db.Integer , db.ForeignKey("admins.id") ,primary_key=True),
    db.Column("day_id",db.Integer , db.ForeignKey("day.id") ,primary_key=True),
)

@dataclass
class Admins(db.Model):
    id:int
    name:str
    password:str
    email:str

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    admin_day = db.relationship('Day',secondary=admin_day,backref='admin_day')

@dataclass
class Admindashboard(db.Model):
    id:int
    title:str
    description:str
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    description = db.Column(db.Text,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)

@dataclass
class Day(db.Model):
    id:int
    title:str

    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(80),nullable=False)


