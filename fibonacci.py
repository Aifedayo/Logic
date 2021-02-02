def Fib():
    """
    Fibonacci Sequence to Infinity
    """
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b
