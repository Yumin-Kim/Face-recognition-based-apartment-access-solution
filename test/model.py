from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Members(db.Model):
    __tablename__ = 'test'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(20, 'utf8mb4_unicode_ci'))
    email = db.Column(db.String(50, 'utf8mb4_unicode_ci'))

    def __init__(self, username, email, phone, start, end):
        self.username = username
        self.email = email