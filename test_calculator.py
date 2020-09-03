# Created a virtual environment

# Writing a function to test imported module
# Do not import functions that require user-interface interaction


# This test file should be a .py file
# Has to be


# Option 1: Multiple assert statements in one test function -- least desirable method
"""
def test_check_HDL(): # name the test function as test_<name of function your are importing>
    from calculator import check_HDL #must it be this syntax? or can I do import _______ from ___________
    result = check_HDL(70)   # Enter a value into the function you imported and store it as a result 
    expected = "Normal" # must know your original function's expected output.
    assert result == expected # Assert checks for boolean condition that you enter

    result = check_HDL(1)
    expected = "Low"
    assert result == expected

    result = check_HDL(45)
    expected = "Borderline Low"
    assert result  == expected  # option 1 for multi-stage unit testing of a function you import that can have various outputs

    # Note that the above uses assert 3 different times
    # Not always a good idea to code this way because if an error occurs in upstream assert statement
    # The code below that isn't ran --> getting incomplete coverage
"""

# Option 2: 3 separate tests via 3 separate test functions
# Ensure names are different or else python would run only the last test with the same name

"""
def test_check_HDL_1(): 
    from calculator import check_HDL 
    result = check_HDL(70) 
    expected = "Normal" 
    assert result == expected 


def test_check_HDL_2():
    from calculator import check_HDL
    result = check_HDL(1)
    expected = "Low"
    assert result == expected


def test_check_HDL_3(): 
    from calculator import check_HDL 
    result = check_HDL(45)
    expected = "Borderline Low"
    assert result  == expected
    
    
    # This method is okay but it requires copying and pasting which si not efficient and can lead to errors
"""
# Option 3
import pytest

# add decorator # string, then list in parametrize

# The first argument of the decorator is a string of parameters you expect the function in the decorator to take in
# The second arument of the decorator is a list of tuples containing the variables you wanna test
@pytest.mark.parametrize("HDL_test_result, expected", [
    (70, "Normal"),
    (1, "Low"),
    (45, "Borderline Low"),
    ])
def test_check_HDL(HDL_test_result, expected):
    from calculator import check_HDL
    answer = check_HDL(HDL_test_result)
    assert answer == expected

