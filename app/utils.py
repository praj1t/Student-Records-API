import json
import time
import random
from enum import unique


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

def idgen(students):
    while True:
        idform = str(random.randint(1,999999)).zfill(6)
        idnum = int(idform)
        unique = True
        for i in students:
            if i["id"] == idnum:
                unique = False
        if unique ==  True:
            return idnum
        else:
            continue