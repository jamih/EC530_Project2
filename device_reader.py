# Python program to read device json file

import json
# opening json file



# first check that what's loaded from the file or string is 
# a valid json file
# then save the json file to a dict
# check the fields of the dict
# check if it's a string
# check for negative measurements
# check for format for bp
# check that it's a valid string with numbers or letters
def json_read():
    
    valid = json_validate()
    print(valid)
    if(valid):
        f = open('device_example.json')
        # returns JSON object as a dictionary
        data = json.load(f)
        print(data)
    else:
        exit()

   
    #return data

def json_validate():
    f = open('device_example.json')
    
    # throw ValueError if string or data passed can't be
    # decoded as json
    try: 
        json.load(f)
    except ValueError as err:
        return False
    return True

     # closing file
    f.close()


def main():
    #print(json_read())
    json_read()
    #json_validate()


if __name__ == '__main__':
    main()