"""

 Description:
 Array
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

# System Libraries
import numpy as np


#  ==========================================================================================================
#  Python List
#  ==========================================================================================================

# ----------------------------------------------------
# Create
# ----------------------------------------------------
list1 = [1, 2.2, "3"]

# ----------------------------------------------------
# Access
# ----------------------------------------------------
list1[0]
list1[-1]

# ----------------------------------------------------
# Methods
# ----------------------------------------------------
list1.append(4)  # Add element at the end
list1.prepend(4)  # Add element at the start
list1.insert(4, 1)  # Add element at the position
list1.reverse()  # Reverse elements
list1.extend([97, 98, 99])  # Add elements at the end
list1.pop()  # Remove element at the end
list1.pop(1)  # Remove element at the position
list1.remove(1)  # Remove element with value (NOT INDEX)

# ----------------------------------------------------
# Slicing
# ----------------------------------------------------
list1[:2]  # Slice from 1st to 2nd elements
list1[2:-2]  # Slice from 3rd to 2nd last elements
list1[2:]  # Slice from 3rd to last elements

# ----------------------------------------------------
# Length
# ----------------------------------------------------
len(list1)

# ----------------------------------------------------
# Delete
# ----------------------------------------------------
del list1

# ----------------------------------------------------
# List using List Comprehension
# ----------------------------------------------------
list1 = [x for x in range(10)]

# ----------------------------------------------------
# List using Generator Comprehension
# ----------------------------------------------------
list2 = list((x for x in range(10)))

# ----------------------------------------------------
# List using Range Generator
# ----------------------------------------------------
list3 = list(range(10))

#  ==========================================================================================================
#  Numpy Array
#  ==========================================================================================================

list2 = np.array([1, 2.2, "3"])
list2.tolist()  # Numpy array to python list
list2.size()

#  ==========================================================================================================
#  Dictionary Access
#  ==========================================================================================================

dict1 = {"x": 1, "y": 1.2}
dict1.items()   # Key, Value pair
dict1.keys()    # Keys
dict1.values()  # Values

#  ==========================================================================================================
#  Iterators
#  ==========================================================================================================

# ----------------------------------------------------
# Iterator Protocol
# ----------------------------------------------------
# __iter__(): It returns an iterator object
# __next__(): It returns the next iterator item

# ----------------------------------------------------
# Iterable
# ----------------------------------------------------
# - It doesn't save current state of iteration
# - It implements __item__()
# - It is subscriptable using index
# - It is used with function (return)
iterable1 = list(range(10))
iterable2 = [x for x in range(10)]
iterable3 = list(x for x in range(10))
print(iterable2[1])  # Allowed

# ----------------------------------------------------
# Iterator
# ----------------------------------------------------
# - It saves current state of iteration
# - It implements __item__() and _next__()
# - It is NOT subscriptable using index
# - It is used with generator (yield)
# - StopIteration is raised when all elements are already iterated
iterator1 = range(10)
iterator2 = (x for x in range(10))
iterable3 = iter(iterable1)
for index, element in enumerate(iterator1):
    print(element)
    if index == 4:
        break
print(next(iterator1))  # State of iteration was saved
print(iterator1[1])     # NOT allowed
print(*iterator1)