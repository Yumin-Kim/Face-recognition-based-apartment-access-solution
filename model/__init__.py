# Python에서 제공하는 ORM을 통해서 프로그램을 진행할 예정
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from collections import OrderedDict

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:wjqrmsrma!wl6311@localhost:3306/facerecognition"
    app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4' # utf-8 인코딩
    from model.user_model import Users
    from model.admin_model import Admins,Day,Admindashboard,admin_day
    db.init_app(app)
    return app

class Test_AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
