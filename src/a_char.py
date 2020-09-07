'''Char Module'''
import unittest

def Chars(text:str):
    if type(text) != str:
        raise ValueError
    return len(text)

print(Chars('saya makan'))