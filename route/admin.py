from flask import request , jsonify
from flask_restx import Resource, Api, Namespace
import config as database

Admin = Namespace("admin")


@Admin.route('')
class TodoPost(Resource):
    def get(self):
        db_class = database.Database()
        sql = "SELECT * FROM users"
        row = db_class.execute_all(sql)
        print(row)
        return jsonify(row)
