import os
import sys
import notify2

def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Missing json file path!\n")
        exit(1)

    json_file = sys.argv[1]

    if not os.path.isfile(json_file):
        sys.stderr.write("File doesn't exist!\n")
        exit(1)

if __name__ == "__main__":
    main()