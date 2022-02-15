# Python program to read device json file

import json
# opening json file

def json_check():
    f = open('device_example.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    # iterating through json list

    for i in data:
        print(i)


    # closing file
    f.close()


def main():
    json_check()


if __name__ == '__main__':
    main()