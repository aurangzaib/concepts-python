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
import csv

input_array = [x for x in range(0, 10, 1)]
input_dict = {"x": 1}
filename = "Resources/dummy.csv"


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
function3(array=input_array, dictionary=input_dict)


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
    kwargs["x"], kwargs["y"]
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

# With list comprehension
list2 = [x * 1.1 for x in input_array]
for item in list2:
    print(item)

# With lambda expression
list3 = [lambda x=x: x * 1.1 for x in input_array]
for item in list3:
    print(item())

# ==========================================================================================================
# Map, Filter, Reduce
# ==========================================================================================================

# Map applies the given function/lambda on each element of list
# https://www.geeksforgeeks.org/python-map-function/

# Filter applies given function/lambda on each element of list to filter the data
# https://www.geeksforgeeks.org/filter-in-python/

# Reduce applies the function/lambda on two elements to get a resultant
# This resultant is used as an input for next iteration
# https://www.geeksforgeeks.org/reduce-in-python/

# ----------------------------------------------------
# Using Function
# ----------------------------------------------------

def mapper_(x):
    return x + 0.1

def filter_(x):
    return x if x % 2 == 0 else None

def reducer_(x, y):
    return x + y

map_result1 = list(map(mapper_, input_array))  # Map
filter_result1 = list(filter(filter_, input_array))  # Filter
reduce_result1 = ft.reduce(reducer_, input_array)  # Reduce

# ----------------------------------------------------
# Using Lambda
# ----------------------------------------------------

map_result2 = list(map(lambda x: x + 0.1, input_array))  # Map
filter_result2 = list(filter(lambda x: x % 2 == 0, input_array))  # Filter
reduce_result2 = ft.reduce(lambda x, y: x * y, input_array)  # Reduce

# ==========================================================================================================
# Generator
# ==========================================================================================================
# - It is a lazy function which uses yield instead of return
# - It doesn't store entire content in memory
# - Yield pauses the generator execution
# - Return stops the function execution

file = open(filename, newline="", encoding="utf-8")

# ----------------------------------------------------
# Data Extraction Using Function
# ----------------------------------------------------
def data_extraction_function():
    iterators = csv.reader(file, delimiter=',')    # Iterators
    return list(iterators)                         # Return

# ----------------------------------------------------
# Data Extraction Using Generator
# ----------------------------------------------------
def data_extraction_generator():
    iterators = csv.reader(file, delimiter=',')    # Iterators
    for row in iterators: yield row                # Yield

# ----------------------------------------------------
# Data Processing Using Function
# ----------------------------------------------------
rows_iterable = data_extraction_function()
for row in rows_iterable:
    print("ID: {} Name: {}".format(row[1], row[2]))

# ----------------------------------------------------
# Data Processing Using Generator
# ----------------------------------------------------
rows_iterator = data_extraction_generator()
for row in rows_iterator:
    print("ID: {} Name: {}".format(row[1], row[2]))

# ==========================================================================================================
# Closure
# ==========================================================================================================

# ==========================================================================================================
# Decorator
# ==========================================================================================================

# ==========================================================================================================
# Memoization
# ==========================================================================================================
