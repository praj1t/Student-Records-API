import json
import time
import random

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

