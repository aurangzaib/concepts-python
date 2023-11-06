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
from dataclasses import dataclass
from typing import Callable
import functools
import time
import csv

input_filename = "Resources/dummy.csv"
input_array = list(range(10))
input_dict = {"x": 1}

# ==========================================================================================================
# Link
# ==========================================================================================================
# - https://realpython.com/introduction-to-python-generators/
# - https://www.geeksforgeeks.org/generators-in-python/
# - https://realpython.com/primer-on-python-decorators/

# ==========================================================================================================
# Parameter
# ==========================================================================================================

# ----------------------------------------------------
# Immutable (Copy)
# ----------------------------------------------------
def function1(a, b):
    return a, b, 1

# ----------------------------------------------------
# Mutable (Global)
# ----------------------------------------------------
def function2(a_local, b_local):
    global a

# ----------------------------------------------------
# Mutable (Reference)
# ----------------------------------------------------
def function3(array: list, dictionary: dict, obj: object):
    dictionary["x"] = 99
    # instance.x = 99
    array[0] = 99
    obj['x'] = 99

# ----------------------------------------------------
# Default Value
# ----------------------------------------------------
def function4(a, b, c=1):
    pass

# ----------------------------------------------------
# Keyword
# ----------------------------------------------------
function3(array=input_array, dictionary=input_dict, obj={'x': 0})

# ----------------------------------------------------
# Variadic
# ----------------------------------------------------
# List
def function5(*argv):
    for arg in argv: print(arg)
function5(1, 2, 3)
# Dictlist
def dicts(*dictionaries):
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            print(key, value)
dicts({"x": 1, "y": 2}, {"x": 3, "y": 4})

# ----------------------------------------------------
# Variadic Key-value
# ----------------------------------------------------
def function5(**kwargs):
    kwargs["x"], kwargs["y"]
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))
function5(x=1, y=2)

# ==========================================================================================================
# Lambda Expression
# ==========================================================================================================

# Syntax:
# lambda parameter: expression

a, b = 1, 2

# ----------------------------------------------------
# Lambda vs Function
# ----------------------------------------------------

# Function definition
def max_function(x, y):
    return x if x > y else y
print(max_function(a, b))

# Lambda expression
max_lambda = lambda x, y: x if x > y else y
print(max_lambda(a, b))

# ----------------------------------------------------
# Lambda vs Comprehension
# ----------------------------------------------------

# With list comprehension
list2 = [x * 1.1 for x in input_array]
for item in list2: print(item)

# With lambda expression
list3 = [lambda x=x: x * 1.1 for x in input_array]
for item in list3: print(item())

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

def mapper_(x): return x + 0.1
def filter_(x): return x if x % 2 == 0 else None
def reducer_(x, y): return x + y

map_result1 = list(map(mapper_, input_array))               # Map
filter_result1 = list(filter(filter_, input_array))         # Filter
reduce_result1 = functools.reduce(reducer_, input_array)    # Reduce

# ----------------------------------------------------
# Using Lambda
# ----------------------------------------------------

map_result2 = list(map(lambda x: x + 0.1, input_array))             # Map
filter_result2 = list(filter(lambda x: x % 2 == 0, input_array))    # Filter
reduce_result2 = functools.reduce(lambda x, y: x * y, input_array)  # Reduce

# ==========================================================================================================
# Generator
# ==========================================================================================================

# - It is a lazy function which uses yield instead of return
# - It doesn't store entire content in memory
# - Yield pauses the generator execution
# - Return stops the function execution

file        = open(input_filename, newline="", encoding="utf-8") # File Object
iterators   = csv.reader(file, delimiter=',')                    # Iterators
batch_size  = 10

# -------------------------------------------
# Process Using Generator (Iterator)
# -------------------------------------------

def fetch_batch_using_iterator():
    for index, value in enumerate(iterators):
        if index == batch_size: break
        yield value

def process_batch_using_iterator():
    for index, _ in enumerate(iterators):
        print("Batch: {} ----------------------".format(index))
        batch = fetch_batch_using_iterator()
        for row in batch: print("{}  {}".format(row[1], row[2]))

process_batch_using_iterator()

# -------------------------------------------
# Process Using Function (iterable)
# -------------------------------------------

def fetch_batch_using_iterable(input_list, index):
    effective_batch_size = index * batch_size
    return input_list[effective_batch_size : effective_batch_size + batch_size]

def process_batch_using_iterable():
    input_list = list(iterators)
    n_iteration = int(len(input_list)/batch_size)
    for index in range(n_iteration):
        print("Batch: {} ----------------------".format(index))
        batch = fetch_batch_using_iterable(input_list, index)
        for row in batch: print("{}  {}".format(row[1], row[2]))

process_batch_using_iterable()

# ==========================================================================================================
# Closure
# ==========================================================================================================

# - A nested function returned from inside another function
# - It has access to enclosing function scope even after enclosing function is terminated
# - It is a data hiding mechanism

# ----------------------------------------------------
# Function - No data hiding
# ----------------------------------------------------
def get_from_function():
    data = {'x': 1, 'y': 2}
    return data
data = get_from_function()
print("Using Function: ", data['x'], data['y'])

# ----------------------------------------------------
# Closure - With data hiding
# ----------------------------------------------------
def get_from_closure():
    data = {'x': 1, 'y': 2}
    def _(): return data
    return _
invocable = get_from_closure()
data = invocable()
print("Using Closure: ", data['x'], data['y'])

# ----------------------------------------------------
# Class - No data hiding
# ----------------------------------------------------
class get_from_class:
    def __new__(self):
        self.x, self.y = 1, 2
        return self
data = get_from_class()
print("Using Class: ", data.x, data.y)

# ----------------------------------------------------
# Data Class - No data hiding
# ----------------------------------------------------
@dataclass
class get_from_dataclass:
    x, y = 1,2
data = get_from_dataclass()
print("Using Class: ", data.x, data.y)

# ----------------------------------------------------
# Functor - With data hiding
# ----------------------------------------------------
class get_from_functor:
    def __call__(self):
        self.x, self.y = 1, 2
        return self
instance = get_from_functor()
data = instance()
print("Using Functor: ", data.x, data.y)

# ==========================================================================================================
# Decorator
# ==========================================================================================================

# - It is a function inside a function, like closure
# - It extends input function without modifying it

# ----------------------------------------------------
# Simple Decorator
# ----------------------------------------------------

def simple_decorator(func):
    def wrapper():
        print("Before calling simple decorated function")
        func()
        print("After calling simple decorated function")
    return wrapper

@simple_decorator
def simple_function():
    print("Calling simple function")

simple_function()

# ----------------------------------------------------
# Timer Decorator
# ----------------------------------------------------

def timer(func: Callable):
    @functools.wraps(func)              # Recommended: To retain function information
    def wrapper(*argv, **kwargs):
        t1 = time.perf_counter()        # Start time
        data = func(*argv, **kwargs)    # Call decorated function
        t2 = time.perf_counter()        # End time
        print("{}: {:.10f}ms".format(func.__name__ , t2 - t1))
        return data                     # Return result of decorated function
    return wrapper                      # Return wrapper

@timer 
def get_list_1(): return list(range(10))
@timer
def get_list_2(): return [x for x in range(10)]
@timer
def get_list_3(): return list(x for x in range(10))

get_list_1()
get_list_2()
get_list_3()

# ----------------------------------------------------
# Cascaded Decorators
# ----------------------------------------------------

def decorator1(func):
    def wrapper(): func(), print("decorator 1")
    return wrapper

def decorator2(func):
    def wrapper(): func(), print("decorator 2")
    return wrapper

@decorator2
@decorator1
def function1(): pass

function1()

# ----------------------------------------------------
# Parameterized Decorators
# ----------------------------------------------------

def n_times(n=2):
    def wrapper1(func):
        def wrapper2(*argv, **kwargs):
            for _ in range(n): func(*argv, **kwargs)
        return wrapper2
    return wrapper1

@n_times(n=5)
def function1(input):
    print("Hello World: {}".format(input))

function1(123)

# ----------------------------------------------------
# Slowdown Decorator
# ----------------------------------------------------

def slowdown(t=0):
    def wrapper1(func):
        def wrapper2(*argv, **kwargs):
            data = func(*argv, **kwargs)
            time.sleep(t)
            return data
        return wrapper2
    return wrapper1

@slowdown(t=1)
def printer(param):
    print(param)

counter = 0
for _ in range(10):
    global coutner
    counter+=1
    printer(counter)

# ==========================================================================================================
# Memoization
# ==========================================================================================================
