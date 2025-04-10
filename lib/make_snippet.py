
""""
Example code from tutorial (not Steve's code)
"""
# For tests 1-3
# def make_snippet(text):
#     if "e" in text:
#         index_of_e = text.index("e")
#         letters_before_e = text[:index_of_e]
#         letters_after_e = text[index_of_e + 1:]
#         return f"e{letters_before_e}{letters_after_e}"
#     else:
#        return text
    
# For tests 1-4
# def make_snippet(text):
#     if "e" in text:
#         letter_es = [letter for letter in text if letter == "e"]
#         non_letter_es = [letter for letter in text if letter != "e"]
#         letters = letter_es + non_letter_es
#         return "".join(letters)
#     else:
#        return text

# Alternative version for tests 1-4
def make_snippet(text):
    if "e" in text:
        new_text = ""
        for letter in text:
            if letter == "e":
                new_text= "e" + new_text
            else:
                new_text = new_text + letter
        return new_text
    else:
        return text