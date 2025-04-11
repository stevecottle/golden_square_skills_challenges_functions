# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
So that I can improve my grammar


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def verify_beginning_and_end_of_sentence(mixed_words):
    """
    Parameters:
    Uses a string (sentence) as an argument (input)

    Returns:
    Boolean 
    - True if text starts with capital and ends with full stop
    - False if it doesn't


    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence with a capital letter at the beginning and a full stop at the end
Function returns True
"""
verify_beginning_and_end_of_sentence("This is my test sentence.")
returns = True

"""
Given a sentence with a capital letter at the beginning and no full stop at the end
Function returns False
"""
verify_beginning_and_end_of_sentence("This is my test sentence")
returns = False

"""
Given a sentence with no capital letter at the beginning and a full stop at the end
Function returns False
"""
verify_beginning_and_end_of_sentence("this is my test sentence.")
returns = False
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
