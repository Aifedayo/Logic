"""
A python list that returns a unique list
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1,2,3,4,5]
"""

def unique_list2(mylist):
    newlist = []
    for num in mylist:
        if num not in newlist:
            newlist.append(num)
    print(newlist)

unique_list2([1,2,2,2,3,4,4,4,5])
