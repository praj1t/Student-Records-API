import json

def open_file():
    with open("database.json", 'r') as file:
        return json.load(file)

def write_file(students):
    with open("../database.json", 'w') as file:
        json.dump(students, file)