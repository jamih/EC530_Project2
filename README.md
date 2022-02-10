# EC530_Project2
Remote Health Care App




## Documenting Database Schema

# EC530_Project2
Remote Health Care App




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
User Insurance Lookup Table
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
User Personal Info Table
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








