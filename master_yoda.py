def master_yoda(string):
    """
    A function that return a sentence with the words reversed
    """
    new_string = string.split()[::-1]
    return ' '.join(new_string)

master_yoda('I am home')
