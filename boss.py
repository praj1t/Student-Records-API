import function
import json
import os

#import FreeSimpleGUI as sg

if not os.path.exists("database.json"):
    with open("database.json", 'w') as file:
        json.dump([],file)

# sg.theme("DarkAmber")
report = {}

while True:
    function.print_title()
    print(f"What are you trying to do?" + '\n'
        f"1 - NEW STUDENT DATA" + '\n'
        f"2 - SHOW STUDENT DATA" + '\n'
        f"3 - EXIT" + '\n')
    user_input = input("------> ")

    students = function.open_file()
    match user_input:
        case "1":
            function.get_studentdata(students)
            function.write_file(students)
            print()
        case "2":
            stdname = input("Enter the name of the student or leave it blank to display all: ").capitalize()
            print()
            function.show_studentdata(students,stdname)
            print()
        case "3":
            print("QUITTING PROGRAM NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break


# title = sg.Text("STUDENT DATABASE", size=50)
# add_button = sg.Button("Add")
# show_button = sg.Button("Show")
# close_button = sg.Button("Exit")
# text_box = sg.Input(key="name")
# window = sg.Window("STUDENT DATABASE",
#                    layout = [[title],
#                              [add_button, show_button, close_button],
#                              [text_box]] )
#
# while True:
#     event, values = window.read()
#     students = function.open_file()
#     match event:
#         case "Add":
#             function.add_section()
#             function.get_studentdata(students)
#             function.write_file(students)
#         case "Show":
#             function.show_studentdata(students, "qwerty")
#         case "Exit":
#             break
#         case sg.WIN_CLOSED:
#             break
#     print(event)
#
# window.close()

# students = function.open_file()
#function.show_studentdata(students)
# function.show_studentdata(students, )