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
Patient Insurance Lookup Table
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
Patient Personal Info Table
{
    "First name": (string),
    "Last name": (string),
    "Weight": (Double),
    "Height": (Double),
    "Gender": (String),
    "Address" (string),
    "Medical History": (string),
    "Allergies": (string)
}
```

## Branching Strategy
For this project, I will be using the Github Flow branching strategy.
There will be two types of branches:
* **master** : the primary branch where code is branched off from and merged to. 
* **sub-branches**: any chance (feature, bug) is made in a new branch that is derived from the master. The branch name will indicate what the feature or bug is.
    * When the development of a certain feature or bug is done on that sub-branch, a pull request will be created so that code review can happen. When the code is reviewed and approved, there will be testing before merging on the master branch. The unit tests should run successfully.
 
Source: https://www.bmc.com/blogs/devops-branching-strategies/





