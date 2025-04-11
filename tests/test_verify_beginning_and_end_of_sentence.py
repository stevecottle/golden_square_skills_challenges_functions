from lib.verify_beginning_and_end_of_sentence import *


"""
Given a sentence with a capital letter at the beginning and a full stop at the end
Function returns True
"""
def test_with_a_valid_sentence():
    result = verify_beginning_and_end_of_sentence("This is my test sentence.")
    assert result == True

"""
Given a sentence with a capital letter at the beginning and no full stop at the end
Function returns False
"""
def test_with_a_valid_sentence():
    result = verify_beginning_and_end_of_sentence("This is my test sentence")
    assert result == False

"""
Given a sentence with no capital letter at the beginning and a full stop at the end
Function returns False
"""

def test_with_a_valid_sentence():
    result = verify_beginning_and_end_of_sentence("this is my test sentence.")
    assert result == False