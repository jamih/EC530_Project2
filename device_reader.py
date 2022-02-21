# Python program to read device json file

import json
# opening json file

# first check that what's loaded from the file or string is 
# a valid json file
# then save the json file to a dict


# check if it's a string
# check for negative measurements
# check for format for bp
# check that it's a valid string with numbers or letters

# function that checks the fields of the json file for validity
def json_read():
    
    result = json_validate()
    valid_json  = result[0]
    

    if(valid_json):
        data = (result[1])
    else:
        return False
    
    # check that fields are valid 
    valid_fields = ["Device_ID",  "Device_Name",
    "Type_of_Measurement", "Measurement", "Patient_ID"]
    valid_measurement_fields = ["Unit", "Value"]
    json_fields = list(data.keys())

    if(json_fields!=valid_fields): 
        return False
    
    # check within measurements field if the embedded fields are there 
    else:
        measurement_fields = list(data["Measurement"].keys())
        if(valid_measurement_fields!=measurement_fields):
            return False
    
    # DEVICE ID : check that it's an integer

    if not(isinstance(data.get("Device_ID"), int)):
        return False

    # VALIDATION BY DEVICE NAME
        # if it's a Thermometer, check that the units are k, c, f and value is double
    if (data.get("Device_Name") == "Thermometer"):
        if (not(data["Measurement"]["Unit"]=="f") and (not(data["Measurement"]["Unit"]=="k")) and (not(data["Measurement"]["Unit"]=="c"))):
            print("not a valid temp unit")
        if not(isinstance(data["Measurement"]["Value"], float)):
            print("THERM not a double")
        
        # if it's Sphygmomanometer, check that the units are mmHg and value is int
    if (data.get("Device_Name") == "Sphygmomanometer"):
        if (not(data["Measurement"]["Unit"]=="mmHg")):
            print("invalid spyg unit")

        if not(isinstance(data["Measurement"]["Value"], int)):
            print("SPYGH not an int")
        # if it's an Oximeter, check that the units are bpm and value is int 
        # ADD THE OXYGEN LEVEL THING TO THE OXIMETER JSON FILE AND CHECK FOR IT
    if (data.get("Device_Name") == "Oximeter"):
        if (not(data["Measurement"]["Unit"]=="bpm")):
            print("invalid oxi unit")

        if not(isinstance(data["Measurement"]["Value"], int)):
            print("OXI not an int")
        # if it's a Scale, check that the units are lb or kg and value is double
    if (data.get("Device_Name") == "Scale"):
        if (not(data["Measurement"]["Unit"]=="lb") and (not(data["Measurement"]["Unit"]=="kg"))):
            print("not a valid scale unit")

        if not(isinstance(data["Measurement"]["Value"], float)):
            print("SCALE not an int")
        # if it's a glucometer, check that units are mg/dL and value is int
    if (data.get("Device_Name") == "Glucometer"):
        if (not(data["Measurement"]["Unit"]=="mg/dL")):
            print("invalid glu unit")

        if not(isinstance(data["Measurement"]["Value"], int)):
            print("GLU not an int")

    # PATIENT ID: check that it's an integer


    # Sphygmomanometer, Oximeter, Scale, Glucometer have int values
    # check that thermometer has valid unit fields
    # check that Thermometer has double measurement
    #if(data['Device_name']=="Thermometer"):

    
# function that checks if file is in valid json format
def json_validate():
    f = open('therm2.json')
    
    # throw ValueError if string or data passed can't be
    # decoded as json
    try: 
        data = json.load(f)
        #data = json.load(f)
    except ValueError as err:
        print("failed")
        return False, "invalid json file"
    else:
        #print("it went through")
        #data = json.load(f)
        return True, data

     # closing file
    f.close()

# function to send data to a text file 
def send_data():
    result = json_validate()
    valid_json  = result[0]
    

    if(valid_json):
        data = (result[1])

    with open('sample_data.txt', 'w') as sample_file:
        sample_file.write(json.dumps(data))



    




def main():
    #print(json_read())
    json_read()
    #json_validate()
    send_data()


if __name__ == '__main__':
    main()