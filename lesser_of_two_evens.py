"""
A function that returns the lesser of two given
numbers if both numbers are even, but greater if
one or both numbers are old
"""

def lesser_of_even(number1, number2):
    if number1 and number2 % 2 == 0:
        print(min(number1, number2))
    else:
        print(max(number1, number2))

lesser_of_even(1,3)