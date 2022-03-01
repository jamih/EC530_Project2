import flask
from flask import request, jsonify

application = flask.Flask(__name__)
application.config["DEBUG"] = True


devices = [
    {
    "Device_ID": 1,
    "Device_Name": "Oximeter",
    "Type_of_Measurement": "blood pressure",
    "Measurement": {
        "Unit": "lb",
        "Value": 70
    },
    "Patient_ID": 1
    
    },
    {
    "Device_ID": 2,
    "Device_Name": "Glucometer",
    "Type_of_Measurement": "glucose content",
    "Measurement": {
        "Unit": "mg/dL",
        "Value": 100
    },
    "Patient_ID": 1
    
    },

    {
    "Device_ID": 3,
    "Device_Name": "Scale",
    "Type_of_Measurement": "weight",
    "Measurement": {
        "Unit": "lb",
        "Value": 130.2
    },
    "Patient_ID": 1
    
}

]


@application.route('/', methods=['GET'])
def home():
    return '''<h1>Devices API</h1>
<p>/devices/all will return all devices</p>'''


# A route to return all of the available entries in our catalog.
@application.route('/devices/all', methods=['GET'])
def api_all():
    return jsonify(devices)

@application.route('/devices/post', methods=['POST'])
def post_device():
    content_type = request.headers.get('Content-Type')
    # check if the file sent is in json format
    if (content_type == 'application/json'):
        json = request.get_json()
        #json_device = json["device"]
        #return json_device
        return json
    else:
        return 'Content-Type not supported!'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()