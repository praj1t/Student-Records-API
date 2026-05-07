import json
import PySimpleGUI as sg
import time
import random
sg.theme("DarkAmber")

yellow = "\033[93m"
white = "\033[0m"
red = "\033[91m"

def print_title():
    print(r"""
    ███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗
    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
    ███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   
    ╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   
    ███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   
    ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   
    """)

    print(yellow + r"""
    ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  
    ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
    """ + white)

def open_file():
    with open("database.json", 'r') as file:
        return json.load(file)

def write_file(students):
    with open("database.json", 'w') as file:
        json.dump(students, file)

def get_studentdata(students):

    report = {"name": "",
              "id": 0,
              "marks": {}}

    report["name"] = input("Enter student name: ").capitalize()
    id_gen = str((random.randint(0,999999))).zfill(6)
    report["id"] = int(id_gen)
    subjects = ["English", "Maths", "Physics", "Programming"]
    for i in subjects:
        marks = int(input(f"Enter marks for {i}:") + '\n')
        report["marks"][i] = marks

    students.append(report)
    return students

def average(marks):
    total = sum(marks.values())
    return total/len(marks.keys())

def gradegetter(average):
    if average >= 90:
        return "A"
    elif average > 80:
        return "B"
    elif average > 70:
        return "C"
    elif average > 50:
        return "D"
    else:
        return "F"


def show_studentdata(students, name = ""):
    if name == "":
        for i in students:
            print(yellow +"=" *40)
            print("           STUDENT REPORT CARD")
            print("=" *40 + white)

            print(f"{'Name':<30}:{yellow}{i['name'].upper()}{white}")
            print(f"{'Student ID':<30}:{i['id']}")
            print("-" *40)
            print(f"{'Subject':<25}{'Marks':>10}")
            print("-" *40)

            for subject, mark in i['marks'].items():
                print(f"{subject:<25}{mark:>10}")

            print("-" *40)

            print(f"{'Average Grade':<25}{average(i['marks']):>10.2f}")
            print(f"{'Total Final Grade':<25}{gradegetter(average(i['marks'])):>10}")
            print(red + "=" *40 + white)
    else:
        for i in students:
            if i["name"].capitalize() == name:
                print(yellow + "=" * 40)
                print("           STUDENT REPORT CARD")
                print("=" * 40 + white)

                print(f"{'Name':<30}:{yellow}{i['name'].upper()}{white}")
                print(f"{'Student ID':<30}:{i['id']}")
                print("-" *40)
                print(f"{'Subject':<25}{'Marks':>10}")
                print("-" *40)

                for subject, mark in i['marks'].items():
                    print(f"{subject:<25}{mark:>10}")

                print("-" * 40)

                print(f"{'Average Grade':<25}{average(i['marks']):>10.2f}")
                print(f"{'Total Final Grade':<25}{gradegetter(average(i['marks'])):>10}")
                print(red + "=" *40 + white)
                break
        else:
            print("Name was not found in the database!")

# def add_section():
#     add_title = sg.Text("ENTER NEW STUDENT DETAILS:")
#     add_textbox = sg.Multiline("sample text", size=(60,20))
#     submit = sg.Button("Submit")
#     backoption = sg.Button("Back")
#     area_window = sg.Window("Add Section",
#                             layout=[[add_title],
#                                     [add_textbox],
#                                     [submit, backoption]],
#                             modal=True)
#
#     while True:
#         event, values = area_window.read()
#         match event:
#             case "Submit":
#                 function.write_file(students)
#             case "Back":
#                 break
#             case "Exit":
#                 break
#             case sg.WIN_CLOSED:
#                 break
#         print(event)
#     area_window.close()