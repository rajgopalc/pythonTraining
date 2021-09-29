from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)

class MyController(Resource):
    def get(self):
        return {'PoweredBy': 'The Flask-RESTFul library'}

    def post(self):
        data = request.get_json()
        return {"Data": data['rootKey']}, 201


class Multiplier(Resource):
    def get(self, num1, num2):
        return jsonify({"ValM": num1 * num2})

    def post(self):
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        return {"ValM": num1 * num2}, 201


class IotStatus(Resource):
    def get(self, dev_id):
        conn = sqlite3.connect('fileDB.db')
        cursor = conn.cursor()
        for i in cursor.execute('SELECT * FROM iot_device WHERE device_id =' + str(dev_id)):
            devStatus = i[1]
        cursor.close()
        conn.close()
        return jsonify({"devStatus": str(devStatus)})


api.add_resource(MyController, '/')
api.add_resource(Multiplier, '/multiply', '/multiply/<int:num1>/<int:num2>')
api.add_resource(IotStatus, '/devStatus/<int:dev_id>')
app.run(debug=False)
