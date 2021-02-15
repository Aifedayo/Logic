def macdonald(str):
    """
    A function that capitalizes the first and fourth letters
    """
    mystr = str[:3].capitalize()
    mystr_middle = str[3:].capitalize()
    return mystr+mystr_middle
macdonald('zainab')