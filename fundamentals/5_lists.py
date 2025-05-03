# list ordered and changeable, may have duplicates
# tuple ordered and unchangeable
# set unordered, unchangeable, unindexed, no duplicates
# dictionary ordered and changeable, no duplicates

thislist = ['apple', 'banana', 'orange']
# lists are ordered
length_of_list = len(thislist)

thislist = [5,4,1,'banana'] # mixed type is ok
print(type(thislist)) # class list

# list constructed from tuple
thislist = list(('a','b','c'))

thislist=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# list access
thislist[1] # single element access, can also be used to assign
n=10
a=3
b=12
print(thislist[:n]) # start to n-1
print(thislist[n:]) # n to end
print(thislist[a:b]) # a to b-1
print(thislist[-3:]) # third last to end
thislist[-4:-2] # fourth last to third last

#insertion and replacement
thislist[5:6] = ["apple","banana"] # replace two items with two items
print(thislist)
thislist[10:14]=['watermelon'] # replace four items with one item
print(thislist)

thislist.insert(7,'orange') # insert at index 7
thislist.append('this goes at the end')

thislist.append([1,2,3,4,5]) # this adds the list as a single element of type list
print(thislist)
thislist.extend([1,2,3,4,5]) #this adds each element of the list as a new element
print(thislist)
# extend also works to add tuples, sets, dictionaries to a list

# remove a certain element
thislist.remove('watermelon')
print(thislist)

# remove a certain index
thislist.pop(7)
del thislist[6]
print(thislist)

# clear a list
thislist.clear()

# delete the list
del thislist

thislist=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# iterate over items in the list
for x in thislist:
    y=x

# iterate over the index and val
for ind, val in enumerate(thislist):
    x=ind
    y=val

# iterate using an index
for i in range(len(thislist)):
    x=thislist[i]

# loop with comprehension
[x for x in thislist]

# comprehension is useful for initializing a list
newlist = [x for x in range(10)]
print(newlist)

fruits = ['apple', 'banana', 'watermelon']
newlist = [x if x != "banana" else "orange" for x in fruits] # iterate through fruits replacing banana with orange
print(newlist)

# sorting