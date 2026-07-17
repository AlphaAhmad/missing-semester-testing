# calculator.py


def divide(a, b):
    unused_variable = 10
    if b    == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return   "F"
