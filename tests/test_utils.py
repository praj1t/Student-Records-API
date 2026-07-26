from app.utils import average, gradegetter



def test_average_marks_returns_70():
    marks = {"English": 40, "Maths": 60, "Physics": 80, "Programming": 100}
    result = average(marks)

    assert result == 70

def test_average_marks_returns_fractional_result():
    marks = {"English": 80, "Maths": 81}
    result = average(marks)

    assert result == 80.5

def test_gradegetter_returns_a_at_90_and_above():
    assert gradegetter(90) == "A"
    assert gradegetter(100) == "A"

def test_gradegetter_returns_b_from_80_to_89():
    assert gradegetter(80) == "B"
    assert gradegetter(89) == "B"

def test_gradegetter_returns_c_from_70_to_79():
    assert gradegetter(70) == "C"
    assert gradegetter(79) == "C"

def test_gradegetter_returns_d_from_50_to_69():
    assert gradegetter(50) == "D"
    assert gradegetter(69) == "D"



def test_gradegetter_returns_f_below_50():
    assert gradegetter(49) == "F"
    assert gradegetter(0) == "F"
