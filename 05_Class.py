from dataclasses import dataclass
from enum import Enum

"""
==========================================================================================================
Link
==========================================================================================================
# - https://realpython.com/python-classes

==========================================================================================================
Note
==========================================================================================================

----------------------------------------------------
Dunder (Double underscore)
----------------------------------------------------
__init__  : Constructor
__new__   : Constructor with return value 
__dict__  : All properties and methods of a class
__call__  : Defines functor behaviour 
__str__   : 
__repr__  : 

----------------------------------------------------
Attributes
----------------------------------------------------
- Class property
- Class method

----------------------------------------------------
Instance property
----------------------------------------------------
- It can only be called through instance
- Unique for an instance

----------------------------------------------------
Static property
----------------------------------------------------
- It can be accessed directly using class
- Shared across all instances

----------------------------------------------------
Static method
----------------------------------------------------
- It can be called directly using class
- Shared across all instances
- @staticmethod

----------------------------------------------------
Class method 
----------------------------------------------------
- A method which takes class as an argument rather than self
- @classmethod

----------------------------------------------------
Private property
----------------------------------------------------
- Start a property with __

----------------------------------------------------
Getter/Setter
----------------------------------------------------
- Interface methods for private property
- To avoid direct changes to private property
- @property             -> Read
- @property.setter      -> Write

----------------------------------------------------
Dynamic Attributes
----------------------------------------------------
- Methods/properties can be added on runtime

----------------------------------------------------
Enum Class
----------------------------------------------------
- An iterable class
- Properties can be of any type
- Properties are immutable contants
"""

# ==========================================================================================================
# Class
# ==========================================================================================================

class Cls:

    # Constructor
    def __init__(self, a, b, c):                                                           
        self.a, self.b, self.c = a, b, c        # Public properties
        self.__priv = None                      # Private properties

    # Functor 
    def __call__(self): return {"a": self.a, "b": self.b, "c": self.c, "priv": self.priv}

    # Method 
    def print(self): print(self.a)
    
    # Getter (interface for __priv)
    @property
    def priv(self): return self.__priv
    
    # Setter (interface for __priv)
    @priv.setter
    def priv(self, priv): self.__priv = priv
    
    # Class method 
    @classmethod
    def init(cls, *argv, **kwargs): return cls(*argv, **kwargs) # Calling constructor

# ==========================================================================================================
# Data Class
# ==========================================================================================================

@dataclass
class Complex:
    real: float = 0.0
    imaginary: float = 0.0

class PointCls:
    def __init__(self, complex, x, y, z):
        self.c: Complex = complex
        self.x: int = x
        self.y: int = y
        self.z: int = z

@dataclass
class PointDtCls:
    c: Complex
    x: int = 0.0
    y: int = 0.0
    z: int = 0.0
    def print(self):
        print("{} + {}j".format(self.c.real, self.c.imaginary))

# ==========================================================================================================
# Data Class (Frozen)
# ==========================================================================================================

# ----------------------------------------------------
# Frozen (nested properties are mutable)
# ----------------------------------------------------
@dataclass(frozen=True)
class PointDtClsConstant:
    c: Complex
    X: int = 0.0
    Y: int = 0.0
    Z: int = 0.0
    def print(self):
        print("{} + {}j".format(self.c.real, self.c.imaginary))

# ----------------------------------------------------
# Nested Frozen (nested properties are immutable constants)
# ----------------------------------------------------
@dataclass(frozen=True)
class Constants:
    @dataclass(frozen=True)
    class __Z: A, B, C = 97, 98, 99
    # Public properties
    X, Y, Z = 1, 2, __Z()

# ==========================================================================================================
# Enum Class
# ==========================================================================================================

@dataclass(frozen=True)
class Companies(Enum):
    BMW         = 99.99
    Mercedes    = "Mercedes"
    Porsche     = 101
    Audi        = 102
    VW          = 1 + 3j

    @classmethod
    def method(cls):
        print(cls.BMW.value)

# ==========================================================================================================
# Test For Class
# ==========================================================================================================

def ClassTester():
    # Instance
    instance1 = Cls(1, 2, 3)                    # Using constructor
    instance2 = Cls.init(9, 10, 11)             # Using class method

    # Read/write public properties
    instance1.a = 10
    print("Public property: ", instance1.a)
    print("Public property: ", instance2.a)

    # Read/write private properties through interface
    instance1.priv = 99                          # Write __priv through priv
    print("Private property: ", instance1.priv)  # Read __priv through priv
    instance1._Cls__priv                         # BAD PRACTICE

    # Functor
    print("Functor: ", instance1())

# ==========================================================================================================
# Test For Data Class
# ==========================================================================================================

def DataClassTester():
    complex     = Complex(2,3)
    point       = PointCls(complex, 1, 2, 3)
    pointdc     = PointDtCls(complex, 1, 2, 3)
    pointdcct   = PointDtClsConstant(complex, 1, 2, 3)

    print("{} + {}j".format(point.c.real, point.c.imaginary))
    pointdc.print()
    pointdcct.print()

    point.x     = 3             # Allowed
    pointdc.x   = 3             # Allowed
#   pointdcct.X = 3             # NOT allowed
    pointdcct.c.real = 3  # Allowed

    const       = Constants()
    print(const.X)              # Allowed
#   const.X     = 11            # NOT allowed
#   const.Z.A   = 11            # NOT allowed

# ==========================================================================================================
# Test For Enum Class
# ==========================================================================================================

def EnumClassTester():
    # No instance required for Enum classes
    for company in Companies:
        print("{}:{}".format(company.name, company.value))
    print(Companies.method())

#---------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ClassTester()
    DataClassTester()
    EnumClassTester()