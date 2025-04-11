# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
So that I can manage my time

    """
    It's worth noting the reading time of 1 word is 3.33333333333 seconds (200/60)
    """


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time_for_text(words_to_read):
    """
    Returns a reading time for a given text

    Parameters: (list all parameters and their types)
        - a string of words

    Returns: (state the return value and its type)
        - an extimated reading time (as an integer?, ~~a string?~~)
        - the user story states words per minute so we should return words per minute

    Side effects: (state any side effects)
        ?????
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a single word
Function returns a reading time of one word
"""
reading_time_for_text("hello") => 3.33333333333 

"""
Given two words
Function returns a reading time of two words
"""
reading_time_for_text("hello you") => 6.66666666666


"""
Given no words
Function returns a reading time of zero
"""
reading_time_for_text("") => 0

"""
Given no words
Function returns a reading time of zero seconds
"""
reading_time_for_text("") => "0 seconds"


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
