# lecture-reminder

A Python script that notifies when a lecture is beginning

## How to setup

```cmd
chmod +x lecture-reminder.py # Makes the python script executable
sudo ln -s <directory-path>/lecture-reminder.py /usr/bin/lecture-reminder # Creates a symbolic link to lecture-reminder script
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

## Running
Command:

```cmd

lecture-reminder.py example.json

```

Dependencies:

```
  notify2 >= 0.3.1
```

## NOTE 

Currently this only runs on Linux
