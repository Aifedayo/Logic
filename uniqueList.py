"""
A python list that returns a unique list
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1,2,3,4,5]
"""
def unique_list(mylist):
    mynewlist = set(mylist)
    print(mynewlist)

unique_list([1,1,1,1,2,2,2,4,4,4,5])
"""
Second Method
"""