"""
A function to multiply all numbers in a list
"""

def multiply_list(mylist):
    total = 1
    for num in mylist:
        total += num
    print(total)


mylist = [1,2,4,5]
multiply_list(mylist)