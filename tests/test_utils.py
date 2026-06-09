from app.utils import average
from app.utils import gradegetter

def test_average_marks_returns_70():
    marks = {"English": 40, "Maths": 60, "Physics": 80, "Programming": 100}
    result = average(marks)
    assert result == 70

def test_gradegetter_returns_correct_grades():
    assert gradegetter(95) == "A"
    assert gradegetter(85) == "B"
    assert gradegetter(75) == "C"
    assert gradegetter(60) == "D"
    assert gradegetter(40) == "F"