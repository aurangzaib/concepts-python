"""
==========================================================================================================
Link
==========================================================================================================
# - https://realpython.com/python-classes

==========================================================================================================
Note
==========================================================================================================

----------------------------------------------------
Dundar (Double underscore)
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
- Class methods

----------------------------------------------------
Static method
----------------------------------------------------
- It can be called directly using Class
- Shared across all instances
- @staticmethod

----------------------------------------------------
Instance property
----------------------------------------------------
- It can only be called through instance
- Unique for an instance

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
- Interface methods: To avoid direct changes to private
- @property             -> Read
- @property.setter      -> Write

----------------------------------------------------
Dynamic Attributes
----------------------------------------------------
- Methods/properties can be added on runtime

"""


class Cls:

    # Constructor
    def __init__(self, a, b, c):                                                           
        self.a, self.b, self.c = a, b, c        # Public properties
        self.__priv = None                      # Private properties

    # Functor 
    def __call__(self): return {"a": self.a, "b": self.b, "c": self.c, "priv": self.priv}

    # Method 
    def print(self): print(self.a)
    
    # Getter (interface for priv)
    @property
    def priv(self): return self.__priv
    
    # Setter (interface for priv)
    @priv.setter
    def priv(self, priv): self.__priv = priv
    
    # Class method 
    @classmethod
    def init(cls, *argv, **kwargs): return cls(*argv, **kwargs) # Calling constructor


if __name__ == "__main__":

    # Instance
    instance = Cls(1, 2, 3)                     # Using constructor
    instance2 = Cls.init(9, 10, 11)             # Using class method

    # Read/write public properties
    instance.a = 10
    print("Public property: ", instance.a)
    print("Public property: ", instance2.a)

    # Read/write private properties
    instance.priv = 99                          # Write __priv through priv
    print("Private property: ", instance.priv)  # Read __priv through priv
    instance._Cls__priv                         # BAD PRACTICE

    # Functor
    print("Functor: ", instance())
