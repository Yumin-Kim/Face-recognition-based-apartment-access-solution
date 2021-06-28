from dataclasses import dataclass
from datetime import date

from model import db

admin_day_mapping = db.Table("admin_day_mapping",
    db.Column("admin_id",db.Integer , db.ForeignKey("admins.id") ,primary_key=True),
    db.Column("day_id",db.Integer , db.ForeignKey("days.id") ,primary_key=True),
    db.Column("group_id",db.Integer , db.ForeignKey("groups.id") ,primary_key=True),
)

@dataclass
class Admins(db.Model):
    id:int
    name:str
    password:str
    email:str
    group_id:int

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    admin_day_mapping = db.relationship('Days',secondary=admin_day_mapping,backref='admin_day_mapping')
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    accessMembers = db.relationship("AccessMembers",backref="admins",lazy=True)

@dataclass
class Admindashboards(db.Model):
    id:int
    title:str
    description:str
    createdAt:date
    updatedAt:date
    deletedAt:date
    admin_id:int
    group_id:int

    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    description = db.Column(db.Text,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
    admin_id = db.Column(db.Integer , db.ForeignKey("admins.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)

@dataclass
class Days(db.Model):
    id:int
    name:str

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80),nullable=False)

def insert_adminInfo():
    query = Day(title = "월")
    db.session.add(query)
    db.session.commit()
    return Day.query.all()

