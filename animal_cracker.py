"""
A function that takes two-word string and returns
True if both words begin with the same letter
"""

def animal_cracker(str1, str2):
    if str1[0] == str2[0]:
        print(f'{str1} and {str2} both have the same beginning letter')
    else:
        print(f'{str1} and {str2} does not have the same beginning letter')

animal_cracker('lion', 'lizard')