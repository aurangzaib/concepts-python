"""

 Description:
 Inheritance
 
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
Note
==========================================================================================================

----------------------------------------------------
Composition
----------------------------------------------------

----------------------------------------------------
Aggregation
----------------------------------------------------

----------------------------------------------------
Association
----------------------------------------------------

"""

# ==========================================================================================================
# Base
# ==========================================================================================================

class BaseClass:
    def __init__(self, a, b): self.a, self.__b = a, b
    @property
    def b(self):             return self.__b
    @b.setter
    def b(self, value):      self.__b = value
    def getter(self):        return self.a      # Can also use @property
    def setter(self, value): self.a = value     # Can also use @propertyname.setter
    def printer(self):       print("(a, b): ({}, {})".format(self.a, self.__b))

instance_base = BaseClass(1, 2)
instance_base.setter(11)
instance_base.a = 11.1
instance_base.b = 9
print(instance_base.a)
print(instance_base.b)

# ==========================================================================================================
# Inheritance
# ==========================================================================================================

class SubClassInheritance(BaseClass):
    def __init__(self, a, b): super().__init__(a, b)
    def getter(self):         return super().getter()
    def setter(self, value):  return super().setter(value)
    def printer(self):        print("a:", self.a, "b:", self.b)

instance_sub1 = SubClassInheritance(5, 6)
print(instance_sub1.getter())
instance_sub1.printer()

# ==========================================================================================================
# Composition
# ==========================================================================================================

class SubClassComposition1(BaseClass):
    def __init__(self, a, b): self.base = BaseClass(a, b)
    def getter(self):         return {'a': self.base.a, 'b': self.base.b}
    def setter(self, a, b):   self.base.a, self.base.b = a, b

instance_sub2 = SubClassComposition1(5, 6)
instance_sub2.getter()          # Subclass method
instance_sub2.base.getter()     # Baseclass method
instance_sub2.setter(11.1, 9)   # Subclass method
instance_sub2.base.printer()    # Baseclass method

# ==========================================================================================================
# Composition (Dependency Injection)
# ==========================================================================================================

class SubClassComposition2(BaseClass):
    def __init__(self, base): self.base = base
    # ...

instance_sub3 = SubClassComposition2(BaseClass(5, 6))
