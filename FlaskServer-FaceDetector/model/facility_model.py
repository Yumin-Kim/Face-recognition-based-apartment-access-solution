from dataclasses import dataclass
from datetime import date

from model import db

facility_List_mapping =db.Table("facility_List_mapping",
    db.Column("user_id",db.Integer , db.ForeignKey("users.id"),primary_key=True),
    db.Column("group_id",db.Integer , db.ForeignKey("groups.id"),primary_key=True),
    db.Column("group_by_group_id",db.Integer , db.ForeignKey("group_by_groups.id"),primary_key=True),
    db.Column("facility_info_list_id",db.Integer , db.ForeignKey("facility_infos.id"),primary_key=True),
    db.Column("facility_room_list_id",db.Integer , db.ForeignKey("facility_room_lists.id"),primary_key=True),
    db.Column("facility_tool_list_id",db.Integer , db.ForeignKey("facility_tool_lists.id"),primary_key=True),
)
@dataclass
class FacilityInfos(db.Model):
    id :int
    description:str
    quantiy:int
    createdAt:date
    updatedAt:date
    deletedAt:date
    user_id:int
    group_id:int
    groupBy_id:int
    petition_id:int
    
    id = db.Column(db.Integer , primary_key=True)
    description = db.Column(db.Text,nullable=False)
    quantiy = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)
    petition_id = db.Column(db.Integer , db.ForeignKey("petitions.id"),nullable=False)
    facility_List_mapping = db.relationship('FacilityInfos',secondary=facility_List_mapping,backref='facility_List_mapping')

@dataclass
class FacilityToolLists(db.Model):
    id:int
    name:str
    pricing:int
    stock:int
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
    facility_List_mapping = db.relationship('FacilityToolLists',secondary=facility_List_mapping,backref='facility_List_mapping')

@dataclass
class FacilityRoomLists(db.Model):
    id:int
    title:str
    name:str
    pricing:int
    capacity:int
    employment:int
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    title = db.Column(db.String(80),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    capacity = db.Column(db.Integer,nullable=False)
    employment = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
    facility_List_mapping = db.relationship('FacilityRoomLists',secondary=facility_List_mapping,backref='facility_List_mapping')
