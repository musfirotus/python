def Chars(text):
    if type(text) != str:
        raise ValueError
    else:
        return len(text)