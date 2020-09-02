import pytest

# add decorator # string, then list in parametrize
@pytest.mark.parametrize("number1, number2, expected", [
    (2,3,5),
    (-1, 4, 3),
    (100, 223, 323),
    (0, 3, 3)
    ])

def test_add_1(number1, number2, expected):
    from math_calculator import add
    answer = add(number1, number2)
    assert answer == expected

