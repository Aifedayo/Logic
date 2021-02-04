def palindrome(string):
    '''
    Python function that checks whether a word 
    or phrase is palindrome or not
    '''
    new_string = string.replace(' ','')
    if new_string == new_string[::-1]:
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')

palindrome(input('Enter a string here: '))
