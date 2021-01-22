"""
Fibonacci Sequence to Infinity
"""
def Fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b
