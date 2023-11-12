"""

 Description:
 Class
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

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
- It has no access to class
- @staticmethod

----------------------------------------------------
Class method 
----------------------------------------------------
- It takes class as an argument rather than self
- It has access to class
- @classmethod

----------------------------------------------------
Private property
----------------------------------------------------
- Start a property with __

----------------------------------------------------
Getter/Setter
----------------------------------------------------
- Interface to avoid direct changes to private property
- @property             -> Read
- @propertyname.setter  -> Write

----------------------------------------------------
Dynamic Attributes
----------------------------------------------------
- Methods/properties can be added on runtime

"""

# ==========================================================================================================
# Definition
# ==========================================================================================================

class Cls:

    # Static property
    static_prop = 33

    # Constructor
    def __init__(self, a, b, c):                                                           
        self.a, self.b, self.c = a, b, c        # Public properties
        self.__priv = None                      # Private properties

    # Functor 
    def __call__(self): return {"a": self.a, "b": self.b, "c": self.c, "priv": self.priv}

    # Instance Method 
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

    # Class method 
    @classmethod
    def dict(cls): return cls.__dict__

    # Static method
    @staticmethod
    def static_method(param): return param + 1

# ==========================================================================================================
# Test
# ==========================================================================================================

# Instance
instance1 = Cls(1, 2, 3)                    # Using constructor
instance2 = Cls.init(9, 10, 11)             # Using class method

# Static property
instance1.static_prop
Cls.static_prop

# Static method
instance1.static_method(1)
Cls.static_method(1)

# Instance method
instance1.print()

# Class method
Cls.dict()

# Functor
print("Functor: ", instance1())

# Read/write public property
instance1.a = 10
print("Public property: ", instance1.a)
print("Public property: ", instance2.a)

# Read/write private property through interface
instance1.priv = 99                                 # Write __priv through priv
print("Private property: ", instance1.priv)         # Read __priv through priv
instance1._Cls__priv                                # BAD PRACTICE
