# Created a virtual environment

"""
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
"""




    # Option 2 when testing 
    # Name each test function differently


import pytest

@pytest.mark.parametrize("HDL_test_result, expected", [
    (70, "Normal"),
    (1, "Low"),
    (45, "Borderline Low"),
    ])
def test_check_HDL(HDL_test_result, expected):
    from calculator import check_HDL
    answer = check_HDL(HDL_test_result)
    assert answer == expected

