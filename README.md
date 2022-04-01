# EC530_Project2: Remote Health Care App

## Table of Contents
- [Development](#phases)
- [Database Schemas](#documentation)
- [Measurement Devices Key](#key)
- [Branching Strategy](#branching)


### Phases

Phase 0:   (Due 2/13)
- [x] Setup your Agile environment for the project (including project, GitHub, testing, etc.).
- [x] Setup your branching strategy.

Phase 1:   Device Module (Due 2/13)
- [x] Define Interface for devices to ingest data into the system.
- [x] Implement Shell of the device interface.
- [x] Implement Unit Tests for the module.
- [x] Implement a simulation to send data via an example program to help users of your system.
- [x] Document the interface well.

Phase 2:   (Due 2/22)
- [x] Use Flask or Django as your WEB service platform
- [x] Integrate your module to become a RESTFUL system
- [x] Deploy your system to free [AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc) services or any free cloud of your choosing
- [x] Develop simple WEB applications to test your system.
- [x] Document your REST APIs on your Github

Phase 3:   (Due 3/4)
- [ ] Focus on Chat module
- [ ] Develop...
  - API User Stories for Chat module
  - API definitions for Chat Module
  - REST APIs fro Chat Module
  - Data Model for Chat Module
- [ ] Select best database for such module (document or SQL) and explain why
- [ ] Add it to your project

Phase 4:   (Due 4/19)
- [x] Setup your REACT Native Environment
- [x] Go through REACT native Tutorial
- [ ] Use your REST APIs to build part of the application (add register a user, define a user as a medical professional or patient, have the medical professional add a patient to her/his patient list)
- [ ] Define database model for chat and users
- [ ] Use your REST APIs to develop a chat base on roles (patient can chat with doctor and nurse assigned to them)
- [ ] Familiarize yourself with Healthkit and Google Fit
- [ ] Display Healthkit or Google Fit Data in your app
- [ ] Use your device API to send health data to your backend
- [ ] Nurse or Doctor should be able to see health data of any patient


## Documentation

### Documenting Database Schema

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

### Key
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


## Branching
## Branching Strategy
For this project, I will be using the Github Flow branching strategy.
There will be two types of branches:
* **master** : the primary branch where code is branched off from and merged to. 
* **sub-branches**: any chance (feature, bug) is made in a new branch that is derived from the master. The branch name will indicate what the feature or bug is.
    * When the development of a certain feature or bug is done on that sub-branch, a pull request will be created so that code review can happen. When the code is reviewed and approved, there will be testing before merging on the master branch. The unit tests should run successfully.
 
Source: https://www.bmc.com/blogs/devops-branching-strategies/





