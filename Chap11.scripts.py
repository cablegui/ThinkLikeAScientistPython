# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:04:25 2017

@author: nevil_000
"""

numbers = [17, 123]

numbers[0]

numbers[9-8]



horsemen = ["war", "famine", "pestilence", "death"]

for i in horsemen:
    print(i)
    
len(horsemen)


horsemen = ["war", "famine", ["pestilence", "cocksucker"], "death"]


"cocksucker" in horsemen # Does not work with nested list

"famine" in horsemen



a = ["one", "two", "three"]
del a[1]

a
"""
As you might expect, del causes a runtime error if the index is out of range.
You can also use del with a slice to delete a sublist:
"""
a_list = ["a", "b", "c", "d", "e", "f"]
del a_list[1:5]
a_list



# Copying lists

a = [1,2,3]
b = a

a
b

a[0] = 9

a # Modification on a travels to b
b

a = [1,2,3]
b = a[:]

a[0]=9
a
b # Now modification in a does not travel to b

# Using enumerate

xs = [1, 2, 3, 4, 5]

for (i, val) in enumerate(xs):
    xs[i] = val**2
    
xs    

xs.append(20)

xs
>>> mylist.insert(1, 12)  # Insert 12 at pos 1, shift other items up
>>> mylist
[5, 12, 27, 3, 12]
>>> mylist.count(12)       # How many times is 12 in mylist?
2
>>> mylist.extend([5, 9, 5, 11])   # Put whole list onto end of mylist
>>> mylist
[5, 12, 27, 3, 12, 5, 9, 5, 11])
>>> mylist.index(9)                # Find index of first 9 in mylist
6
>>> mylist.reverse()
>>> mylist
[11, 5, 9, 5, 12, 3, 27, 12, 5]
>>> mylist.sort()
>>> mylist
[3, 5, 5, 5, 9, 11, 12, 12, 27]
>>> mylist.remove(12)             # Remove the first 12 in the list
>>> mylist
[3, 5, 5, 5, 9, 11, 12, 27]


a = "Hello World"

b = list(a)

b
",".join(b)