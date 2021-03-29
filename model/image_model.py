from dataclasses import dataclass
from datetime import date

from model import db

user_image_mapping =db.Table("user_image_mapping",
    db.Column("user_id",db.Integer , db.ForeignKey("users.id"),primary_key=True),
    db.Column("group_id",db.Integer , db.ForeignKey("groups.id"),primary_key=True),
    db.Column("group_by_group_id",db.Integer , db.ForeignKey("group_by_groups.id"),primary_key=True),
    db.Column("image_id",db.Integer , db.ForeignKey("images.id"),primary_key=True),
)

outteruser_image_mapping = db.Table("outteruser_image_mapping",
    db.Column("user_id",db.Integer , db.ForeignKey("users.id"),primary_key=True),
    db.Column("group_id",db.Integer , db.ForeignKey("groups.id"),primary_key=True),
    db.Column("group_by_group_id",db.Integer , db.ForeignKey("group_by_groups.id"),primary_key=True),
    db.Column("admin_id",db.Integer , db.ForeignKey("admins.id"),primary_key=True),
    db.Column("image_outter_id",db.Integer , db.ForeignKey("image_outters.id"),primary_key=True),
)

@dataclass
class Images(db.Model):
    id:int
    name:int
    imageCount:int
    createdAt:date
    updatedAt:date

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer,  nullable=False)
    imageCount = db.Column(db.Integer,  nullable=False)
    createdAt = db.Column(db.DateTime,  nullable=False)
    updatedAt = db.Column(db.DateTime,  nullable=True)

@dataclass
class ImageOutters(db.Model):
    id:int
    name:int
    imageCount:int
    createdAt:date
    updatedAt:date

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer,  nullable=False)
    imageCount = db.Column(db.Integer,  nullable=False)
    createdAt = db.Column(db.DateTime,  nullable=False)
    updatedAt = db.Column(db.DateTime,  nullable=True)


