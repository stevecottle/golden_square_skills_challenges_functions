from lib.count_words import *

"""
count_words returns an input of an empty string
"""

# def test_function_returns_empty_string():
#     result = count_words("")
#     assert result == ""


# """
# count_words returns an input of a string of words
# """

# def test_function_returns_string_of_words():
#     result = count_words("first morning")
#     assert result == "first morning"


"""
count_words can return the count of a one word string
"""

def test_function_returns_count_of_one_word_string():
    result = count_words("grace")
    assert result == 1



"""
count_words return the count a multi-word string
"""

def test_function_returns_ctest_function_returns_count_of_multi_word_string():
    result = count_words("fire thought rich meat furlong")
    assert result == 5