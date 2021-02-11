def makes_twenty(num1, num2):
    """
    A function that return True if the sum of the integers is 20
    or if one of the integers is 20
    """
    if num1 + num2 == 20:
       return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False

makes_twenty(13,8)
