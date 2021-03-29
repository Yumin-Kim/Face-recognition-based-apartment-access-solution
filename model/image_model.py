from dataclasses import dataclass
from model import db

@dataclass
class Image(db.Model):
    id:int
    name:int
    imageCount:int
    createdAt:date
    updatedAt:date

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer,  nullable=False)
    imageCount = db.Column(db.Integer,  nullable=False)
    craetedAt = db.Column(db.DateTime,  nullable=False)
    updatedAt = db.Column(db.DateTime,  nullable=True)
    deletedAt = db.Column(db.DateTime,  nullable=True)
    
@dataclass
class ImageOutter(db.Model):
    id:int
    name:int
    createdAt:date
    updatedAt:date

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer,  nullable=False)
    imageCount = db.Column(db.Integer,  nullable=False)
    craetedAt = db.Column(db.DateTime,  nullable=False)
    updatedAt = db.Column(db.DateTime,  nullable=True)


