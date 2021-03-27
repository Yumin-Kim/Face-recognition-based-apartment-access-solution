# Python에서 제공하는 ORM을 통해서 프로그램을 진행할 예정
from sqlalchemy import MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask()
    db.init_app(app)
    import model.test
    with app.app_context():
        db.create_all()


def my_function():
    with create_app().app_context():
        query = Test(username="adaasdasdsas",email="heloasasdasddasd@naverasdasdasd.com")
        db.session.add(query)
        db.session.commit()
# print()

# peter = User.query.filter_by(username="peter").first()
# print(peter.id)