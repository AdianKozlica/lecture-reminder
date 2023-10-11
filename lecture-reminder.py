from datetime import datetime

import os
import sys
import json
import notify2

def get_current_day_and_time():
    date = datetime.now()

    day = date.strftime("%a")
    hours_minutes = date.strftime("%H:%M")

    return day, hours_minutes


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Missing json file path!\n")
        exit(1)

    json_file = sys.argv[1]

    if not os.path.isfile(json_file):
        sys.stderr.write("File doesn't exist!\n")
        exit(1)

    with open(json_file) as file:
        json_dict = json.load(file)

if __name__ == "__main__":
    main()