from urllib import response
import flask
from flask import request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
import device_reader


app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://jamih:test@cluster0.wluiq.mongodb.net/health-care-app?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def home():
    return '''<h1>Devices API</h1>'''


@app.route('/get_devices', methods=['GET'])
def get_devices():
    measurements = mongo.db.devices.find()
    response = json_util.dumps(measurements)
    return Response(response, mimetype='application/json')


@app.route('/devices', methods=['POST'])
def create_device():

    print("One")
    # Receiving data
    data = request.get_json()

    mongo.db.devices.insert_one(data)

    print("Two")

    print(data)
    device_ID = data['Device_ID']
    device_name = data['Device_Name']
    type_of_measurement = data['Type_of_Measurement']
    m_unit = data['Measurement']['Unit']
    m_value = data['Measurement']['Value']
    patient_id = data['Patient_ID']

    if device_ID and device_name and type_of_measurement and m_unit and m_value and patient_id:
        print('found')
    else:
        return not_found()

    json_data = jsonify({'Device_ID': device_ID,'Device_Name': device_name, 'Type_of_Measurement': type_of_measurement,
    'Measurement': {'Unit': m_unit, 'Value': m_value},
    'Patient_ID': patient_id })

    return json_data

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found' + request.url,
        'status': 404
    }


    

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()