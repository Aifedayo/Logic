"""
A function to check if a string is pangram or not
"""
import string

def pangram(str1):
    alphabet = string.ascii_lowercase
    alphaset = set(alphabet)
    mystr1 = set(str1)
    print(mystr1)
    print(alphaset)
    if mystr1 == alphaset:
        print(f'{str1} is a pangram')
    else:
        print(f'{str1} is not a pangram')

pangram(str1='The quick brown fox jumps over the lazy dog')
