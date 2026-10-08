from calculator import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2.5, 1.5) == 4


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(5.5, 2.5) == 3


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-4, 5) == -20
    assert multiply(2.5, 2) == 5
