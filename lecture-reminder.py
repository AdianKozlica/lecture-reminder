from datetime import datetime
from pathlib import Path

import os
import sys
import json
import time
import notify2

ICON_PATH = str(Path(__file__).parent / "img/book.png")

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

    notify2.init("lecture-reminder")

    while True:
        time.sleep(1)

        day, hours_minutes = get_current_day_and_time()
        lecture = json_dict.get(day).get(hours_minutes)

        if not lecture:
            continue
        
        n = notify2.Notification("Lecture", f"Lecture {lecture} is beginning", ICON_PATH)
        n.show()

        time.sleep(60)

if __name__ == "__main__":
    main()