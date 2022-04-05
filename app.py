from urllib import response
from flask import Flask
from flask import request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
import device_reader
from flask import render_template



app = Flask(__name__)
from user import  routes
app.config["MONGO_URI"] = "mongodb+srv://jamih:test@cluster0.wluiq.mongodb.net/health-care-app?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('homepage.html')


# returns all the devices in the database
@app.route('/devices', methods=['GET'])
def all_devices():
    measurements = mongo.db.devices.find()
    response = json_util.dumps(measurements)
    return Response(response, mimetype='application/json')

# returns a specific device, specified by the device ID
@app.route('/device/<device_ID>', methods=['GET'])
def get_device(device_ID):
    device = mongo.db.devices.find_one({"Device_ID": int(device_ID)})
    #measurements = mongo.db.devices.find()
    #if device == null:
    #    return not_found()
    print(device)
    #else:
    response = json_util.dumps(device)
    #return device
    return Response(response, mimetype='application/json')

# posts a device if it's in the right format and validation is successful
@app.route('/device', methods=['POST']) 
def create_device():

    # Receiving data
    data = request.get_json()

    error_code = device_reader.json_validate(data)
    print('ERROR CODE', error_code)
    #print('hello')
    if(error_code==0):
        mongo.db.devices.insert_one(data)
    
    else:
        return Response('INVALID JSON FILE!', status=400, mimetype='application/json')


    #return Response(str(error_code), status=404, mimetype='application/json')
    
    device_ID = data['Device_ID']
    device_name = data['Device_Name']
    type_of_measurement = data['Type_of_Measurement']
    m_unit = data['Measurement']['Unit']
    m_value = data['Measurement']['Value']
    patient_id = data['Patient_ID']

    
    # if device_ID and device_name and type_of_measurement and m_unit and m_value and patient_id:
    #     print('found')
    # else:
    #     return not_found()
    
    
    json_data = jsonify({'Device_ID': device_ID,'Device_Name': device_name, 'Type_of_Measurement': type_of_measurement,
    'Measurement': {'Unit': m_unit, 'Value': m_value},
    'Patient_ID': patient_id })

    return json_data

@app.route('/device/<device_ID>', methods=['DELETE']) 
def delete_device(device_ID):
    delete_device = mongo.db.devices.delete_one({"Device_ID": int(device_ID)})

    if delete_device.deleted_count > 0:
        return "Device " + device_ID + " was deleted"
    else:
        return "", 404

@app.route('/devices', methods=['DELETE']) 
def delete_all():

    x = mongo.db.devices.delete_many({})

    return "all documents were deleted"

    
# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'message': 'Resource Not Found' + request.url,
#         'status': 404
#     }


    

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()

