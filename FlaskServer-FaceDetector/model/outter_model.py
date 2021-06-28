from dataclasses import dataclass
from datetime import date

from model import db
from model.image_model import outteruser_image_mapping
#1대다관계 정의

@dataclass
class OutterUsers(db.Model):
    id:int
    name:str
    description:str
    createdAt:date
    updatedAt:date
    phoneNumber:str
    user_id:int
    group_id:int
    groupBy_id:int
    admin_id:int
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(300),nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    phoneNumber = db.Column(db.String(30),nullable=False)
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)
    admin_id = db.Column(db.Integer , db.ForeignKey("admins.id"),nullable=False)
    accessMembers = db.relationship("AccessMembers",backref="outter_users",lazy=True)
    outteruser_image_mapping = db.relationship('OutterUsers',secondary=outteruser_image_mapping,backref='outteruser_image_mapping')
    
