import pytest

from calculator import add, divide, exponentiate, subtract, multiply


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, 3, 1),
        (2.5, 1.5, 4),
        (0, 0, 0),
        (-2, -3, -5),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (3, 5, -2),
        (5.5, 2.5, 3),
        (0, 5, -5),
        (-3, -2, -1),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 5, 20),
        (-4, 5, -20),
        (2.5, 2, 5),
        (0, 5, 0),
        (-3, -2, 6),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_division():
    assert divide(20, 2) == 10


def test_division_w_remainder():
    assert divide(7, 2) == 3.5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_exponentiation():
    assert exponentiate(2, 3) == 8


def test_exponentiation_to_zero():
    assert exponentiate(5, 0) == 1


def test_exponentiation_with_negative_power():
    assert exponentiate(2, -2) == 0.25
