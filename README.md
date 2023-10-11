# lecture-reminder

A Python script that notifies when a lecture is beginning

Example command:

```cmd

lecture-reminder.py lectures.json

```

JSON Example:

```json

{
    "Mon": {
        "13:00": "Example Lecture"
    },
    "Tue": {
      "14:00": "Example Lecture",
      "15:00": "Example Lecture2"
    },
    "Wed": {},
    "Thu": {},
    "Fri": {},
    "Sat": {},
    "Sun": {}
}

```

Dependencies:

```
  notify2 >= 0.3.1
```

## NOTE 

Currently this only runs on Linux
