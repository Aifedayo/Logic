"""
A function to check if a string is pangram or not
"""
import string

def pangram(str1):
    alphabet = string.ascii_lowercase
    alphaset = set(alphabet)
    #print(alphabet)

pangram(str1='Hello')
