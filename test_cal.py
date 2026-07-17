from gradeapp import divide, get_grade


def test_divide():
    assert divide(10, 2) == 5

def test_grade():
    assert get_grade(90) == "A"
    assert get_grade(80) == "B"
    assert get_grade(70) == "C"
    assert get_grade(60) == "F"
