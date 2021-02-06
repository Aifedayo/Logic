def animal_cracker(string):
    """
    A function that takes two-word string and returns
    True if both words begin with the same letter
    """

    mystring = string.lower().split(' ')

    if mystring[0][0] == mystring[1][0]:
        print(f'{mystring} both have the same beginning letter')
    else:
        print(f'{mystring} does not have the same beginning letter')

animal_cracker('Levelhead llama')
