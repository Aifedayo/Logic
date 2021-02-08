def range_check(num, low, high):
    """
    Here is a func that checks whether a number is in a given range
    """

    if num in range(low, high+1):
        print (f'{num} is in the range of {low} and {high}')
    else:
        print(f'{num} is outside the range')

range_check(5,2,9)
