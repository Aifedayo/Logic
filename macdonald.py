def macdonald(str):
    """
    A function that capitalizes the first and fourth letters
    """
    if len(str) > 3:
        mystr = str[:3].capitalize()
        mystr_middle = str[3:].capitalize()
        return mystr+mystr_middle
    else:
        return f'String too short'
macdonald('zainab')
