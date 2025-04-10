from lib.make_snippet import *

"""
make_snippet takes an empty string and returns an empty string
"""
def test_function_returns_empty_string():
    result = make_snippet("")
    assert result == ""

"""
make_snippet return a string with characters containing no 'e'
"""

def test_function_with_characters_containing_no_e():
    result = make_snippet("wfscgdvhybjgkn")
    assert result == "wfscgdvhybjgkn"

"""
make_snippet takes input of a string with one 'e' in it, and outputs the same string but with the 'e' being located to the start
"""
def test_function_rteruns_string_with_e_at_the_start():
    result = make_snippet("bed")
    assert result == "ebd"

"""
make_snippet takes input of a string with more than one 'e' and outputs the same string but with all 'e's' being located to the start
"""

def test_function_rteruns_string_with_all_es_at_the_start():
    result = make_snippet("bede")
    assert result == "eebd"