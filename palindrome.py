'''
Python function that checks whether a word 
or phrase is palindrome or not
'''

def palindrome(string):
    new_string = string.replace(' ','')
    if string == string[::-1]:
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')

palindrome('vata')
