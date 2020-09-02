# Created a virtual environment

def test_check_HDL():
    from calculator import check_HDL #must it be this syntax
    result = check_HDL(70)   # Enter a value into the function you imported and store it as a result 
    expected = "Normal"
    assert result == expected

    result = check_HDL(1)
    expected = "Low"
    assert result == expected

    result = check_HDL(45)
    expected = "Borderline Low"
    assert result  == expected  # option 1 for multi-stage unit testing of a function you import that can have various outputs





    # Option 2 when testing 
    # Name each test function differently



# import pytest

# add decorator # string, then list in parametrize
@pytest.mark.parametrize("number1, number2, expected", [
    (2,3,5),
    (-1, 4, 3),
    (100, 223, 323),
    (0, 3, 4)
    ])

def test_add_1(number1, number2, expected):
    from math_calculator import add
    answer = add(number1, number2)
    assert answer == expected
