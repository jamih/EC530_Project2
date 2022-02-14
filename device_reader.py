# Python program to read device json file

import json
# opening json file
f = open('device_example.json')

# returns JSON object as a dictionary
data = json.load(f)

# iterating through json list

for i in data['devices']:
    print(i)


# closing file
f.close()