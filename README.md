# EC530_Project2: Remote Health Care App


## Documenting Database Schema

```
Table User Verification (Check which type of user you are)
{
  "UserID": (string),
  "Admin": (boolean),
  "Medical Professional": (boolean),
  "Patient": (boolean)
}
```

```
Table Patient Insurance Lookup 
{
    "First Name": (string),
    "Last Name": (string),
    "Date of Birth": (string),
    "Insurance": {
        "Insurance Name": (string),
        "GroupID": (string)
    },
    "Primary Care Physician": (string)
}
```

```
Table Patient Personal Info 
{
    "First name": (string),
    "Last name": (string),
    "Weight": (double),
    "Height": (double),
    "Gender": (string),
    "Address" (string),
    "Medical History": (string),
    "Allergies": (string)
}
```

``` 
Table Device 
{
    "Device Name": (string),
    "Device ID": (string),
    "Assignee": (string),
    "Assignee ID": (string),
    "Type of Measurement": (string),
    "Unit of Measure": (string),
    "Value of Measurement": (double)
    
    
}
```

### Measurement Devices Key
| Device Name | What it Measures| Unit of Measure | Example of Measurement |
| ------------| ----------------| ------------------------------| --------------|
|Thermometer | temperature | Fahrenheit/Celsius/Kelvin (degrees) | 92.3 |
| Sphygmomanometer| blood pressure | units of millimeters of mercury (mmHg)  | 132/88 mmHg
| Pulse Oximeter | pulse, oxygen saturation | beats per minute (bpm), oxygen saturation (SpO2) | 70 bpm, 96% | 
|Scale | weight | pounds (lb) | 130 lb |
| Glucometer | glucose content in blood, blood sugar levels | milligrams of glucose per decileter of blood (mg/dL) | 100 mg/dL |

### Error Codes Key
| Error Code | Meaning |
| -----------| ---------| 
| 0 | NO ERRORS |
| 1  | INVALID JSON FILE |
| 2 | MISSING FIELDS IN JSON FILE | 
| 3 | INVALID DATA TYPE IN JSON FILE|
|4| MEASUREMENT OUT OF RANGE|
|5| WRONG UNIT|


## Branching Strategy
For this project, I will be using the Github Flow branching strategy.
There will be two types of branches:
* **master** : the primary branch where code is branched off from and merged to. 
* **sub-branches**: any chance (feature, bug) is made in a new branch that is derived from the master. The branch name will indicate what the feature or bug is.
    * When the development of a certain feature or bug is done on that sub-branch, a pull request will be created so that code review can happen. When the code is reviewed and approved, there will be testing before merging on the master branch. The unit tests should run successfully.
 
Source: https://www.bmc.com/blogs/devops-branching-strategies/





