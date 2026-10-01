from calculator import add_numbers, subtract_numbers


def test_addition():
    assert add_numbers(2, 3) == 5


def test_subtraction():
    assert subtract_numbers(5, 3) == 2