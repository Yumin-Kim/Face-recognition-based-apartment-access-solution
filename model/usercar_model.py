from model import db
authors = db.Table('authors',
    db.Column('author_id',db.Integer,db.ForeignKey('author.id'),primary_key=True),
    db.Column('topic_id',db.Integer,db.ForeignKey('topic.id'),primary_key=True)
) 

class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    topics = db.relationship('Topic',secondary=authors,backref='authors')

class Topic(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    name = db.Column(db.String(50))