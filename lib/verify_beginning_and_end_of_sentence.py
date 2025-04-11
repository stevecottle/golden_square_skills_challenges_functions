


def verify_beginning_and_end_of_sentence(sentence):
    if (sentence[-1] == ".") and (sentence[0].isupper()):
        return True
    else:
        return False
