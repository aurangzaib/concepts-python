"""

 Description:
 Function
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

import functools as ft

# ==========================================================================================================
# Immutable Parameter (Value)
# ==========================================================================================================
def function1(a, b):
    return a, b, 1

# ==========================================================================================================
# Immutable Parameter (Reference)
# ==========================================================================================================
def function2(a_copy, b):
    global a  # Reference

# ==========================================================================================================
# Mutable Parameter (Reference)
# ==========================================================================================================
def function3(array, dictionary):
    array[0] = 99
    dictionary["x"] = 99

# ==========================================================================================================
# Parameter default value
# ==========================================================================================================
def function4(a, b, c=1):
    pass

# ==========================================================================================================
# Parameter keyword
# ==========================================================================================================
arr1 = [1, 2, 3]
dict1 = {"x": 1}
function3(array=arr1, dictionary=dict1)

# ==========================================================================================================
# Variadic Parameter
# ==========================================================================================================
def function5(*argv):
    for arg in argv:
        print(arg)

function5(1, 2, 3)

# ==========================================================================================================
# Variadic Key-value Parameter
# ==========================================================================================================
def function5(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

function5(x=1, y=2)

# ==========================================================================================================
# Lambda vs Function
# ==========================================================================================================

# Syntax:
# lambda parameter: expression

a, b = 1, 2

# Function definition
def max_function(x, y):
    return x if x > y else y
print(max_function(a, b))

# Lambda expression
max_lambda = lambda x, y: x if x > y else y
print(max_lambda(a, b))

# ==========================================================================================================
# Lambda vs Comprehension
# ==========================================================================================================

list1 = [1, 2, 3]

# With list comprehension
list2 = [x * 1.1 for x in list1]
for item in list2:
    print(item)

# With lambda expression
list3 = [lambda x=x: x * 1.1 for x in list1]
for item in list3:
    print(item())

# ==========================================================================================================
# Filter
# ==========================================================================================================

# Filter applies given function/lambda on each element of list to filter the data
# https://www.geeksforgeeks.org/filter-in-python/

def get_even_number1(input):
    if input % 2 == 0: return input
def get_even_number2(input, output=[]):
    for element in input:
        output.append(element) if element % 2 == 0 else None
    return output

whole_numbers = [x for x in range(0, 10, 1)]
even_numbers1 = list(filter(lambda x: x % 2 == 0, whole_numbers))
even_numbers2 = list(filter(get_even_number1, whole_numbers))
even_numbers3 = get_even_number2(whole_numbers)

# ==========================================================================================================
# Map
# ==========================================================================================================

# -Map applies the given function/lambda on each element of list
# -https://www.geeksforgeeks.org/python-map-function/

def mapper(input):
    return input + 0.1
input_array = [x for x in range(0, 10)]
output_array1 = list(map(mapper, input_array))
output_array2 = list(map(lambda x: x + 0.1, input_array))

# ==========================================================================================================
# Reduce
# ==========================================================================================================

# Reduce applies the function/lambda on two elements to get a resultant
# This resultant is used as an input for next iteration
# https://www.geeksforgeeks.org/reduce-in-python/

def reducer(input1, input2):
    print(input1, input2)
    return input1 + input2

input_array = [x for x in range(1, 10)]
output1 = ft.reduce(reducer, input_array)
output2 = ft.reduce(lambda x, y: x + y, input_array)

