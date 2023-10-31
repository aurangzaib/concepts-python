"""

 Description:
 Basic
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

# System Libraries
# import antigravity
import numpy as np
import math


# __name__ is a conditional check
# It makes sure the snippet runs only when the file is directly called
if __name__ == "__main__":
    a, b, c = 11.23444, 2, 3, [1, 2, 3]

    #  ==========================================================================================================
    #  Print
    #  ==========================================================================================================
    # Print w/o new line
    print("Hello World", end=" ")
    # Print formatter
    print("a: {}, b: {}, c: {}".format(a, b, c))
    print("{:2.3f}".format(a))

    #  ==========================================================================================================
    #  Any/All
    #  ==========================================================================================================
    a, b, c = True, False, False
    print(any((a, b, c)))  # any one of them should be true
    print(all((a, b, c)))  # all of them should be true

    #  ==========================================================================================================
    #  Ceil/Floor
    #  ==========================================================================================================
    a = 2.333
    print(math.ceil(a))  # integer, higher value
    print(math.floor(a))  # integer, lower value

    #  ==========================================================================================================
    #  Identity(is)/Equality(==)
    #  ==========================================================================================================
    a is b  # Identity operator: true if a and b both points to same object (Note: it should be avoided)
    a == b  # Equality operator: true if a and b have same value

    #  ==========================================================================================================
    #  Datatypes
    #  ==========================================================================================================
    type_integer    = 2                      # Integer
    type_float      = 2.3                    # Float
    type_complex    = 1 + 2.3j               # Complex
    type_string     = "string"               # String
    type_list       = [1, 2, 3]              # Ordered List (Mutable)
    type_set        = set([1,2,3])           # Unordered List
    type_tuple      = (1, 2, 3)              # Tuple (Immutable)
    type_range      = range(0, 10, 2)        # Range (Immutable)
    type_dict       = {"x": 1, "y": 1.2}     # Dicionary (Mutable)
    type_dictlist   = [{"x": 1}, {"y": 2}]   # Dictionary List (Mutable)
    type_frozen     = frozenset({"x": 1})    # Frozenset (Immutable and Noniterable)
    type_nparray    = np.array([1,2,3])      # Numpy Array (Mutable)

    #  ==========================================================================================================
    #  Datatypes Access
    #  ==========================================================================================================
    type_complex.real, type_complex.imag
    type_list[0], type_list[-1]
    type_tuple[0]
    type_dict["x"]
    type_nparray[0]
