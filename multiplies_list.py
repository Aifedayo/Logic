"""
A function to multiply all numbers in a list
"""

def multiply_list(mylist):
    total_multiple = 1
    total_sum = 0
    for num in mylist:
        total_multiple *= num
        total_sum += num
    print(f'Here is the total multiplies of the list: {total_multiple}')
    print(f'Here is the total sum of the list: {total_sum}')


mylist = [1,2,4,5]
multiply_list(mylist)
