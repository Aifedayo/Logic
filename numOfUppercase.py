"""
A function that accepts a string and calculate
the number of uppercase and lowercase in it
"""

def upper_lower(mystring):
    mydict = {'upper': 0, 'lower': 0}
    for string in mystring:
        if string.isupper():
            mydict['upper'] +=1
        elif string.islower():
            mydict['lower'] +=1
        else:
            pass
    print(mydict)

upper_lower('Hello Mr. Rogers, how are you this fine Tuesday')
        
