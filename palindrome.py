'''
Python function that checks whether a word 
or phrase is palindrome or not
'''

def palindrome(string):
    new_string = string.replace(' ','')
    if string == string[::-1]:
        return f'{string} is a palindrome'

palindrome('madam')
