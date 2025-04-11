from lib.reading_time_for_text import *

""""
1/ Given a single word
Function returns a reading time of one word
"""

def test_function_returns_reading_time_of_one_word():
    result = reading_time_for_text("hello")
    assert result == 3.33333333333


"""
2/ Given two words
Function returns a reading time of two words
"""
def test_function_returns_reading_time_of_two_words():
    result = reading_time_for_text("hello you") 
    assert result == 6.66666666666

"""
3/ Given no words
Function returns a reading time of zero
"""

def test_function_returns_reading_time_of_zero():
    result = reading_time_for_text("")
    assert result == 0.0

# """
# 4/ Given no words
# Function returns a reading time of zero seconds
# """

# def test_function_returns_reading_time_of_zero_seconds():
#     result = reading_time_for_text("")
#     assert result == "0.0 seconds"