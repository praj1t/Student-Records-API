import json
from pathlib import Path


def open_file():
    if not Path("database.json").exists():
        write_file([])

    with open("database.json", 'r') as file:
        try:
            return json.load(file)
        except:
            write_file([])
            return []

def write_file(students):
    with open("database.json", 'w') as file:
        json.dump(students, file)