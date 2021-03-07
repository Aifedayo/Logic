def master_yoda(string):
    """
    A function that return a sentence with the words reversed
    """
    return ' '.join(string.split()[::1])

master_yoda('I am home')
