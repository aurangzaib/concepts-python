"""

 Description:
 Data Class
 
 Modifications:
 ---------------------------------------------------------------------------------------
 Date      Vers.  Comment                                                     Name
 ---------------------------------------------------------------------------------------
 01.10.17  01.00  Created												      Siddiqui
 31.10.23  02.00  Updated												      Siddiqui
 ---------------------------------------------------------------------------------------

"""

from dataclasses import dataclass, field

"""
==========================================================================================================
Note
==========================================================================================================

- Composition is used instead of Inheritance in the examples below
- Initial values can be passed on instantiation (as normal class)
- No constructor needs to be defined
- Frozen properties can be defined

"""

# ==========================================================================================================
# Definition
# ==========================================================================================================

class Complex:
    def __init__(self, r=0, i=0.0):
        self.imaginary = i
        self.real = r
    
@dataclass
class DataClass:
    c : Complex = Complex()
    x : int = 1

@dataclass
class NestedDataClass:
    dt: DataClass = field(default_factory=DataClass)
    y : float = 1.1
    z : int = 0                 # Type attribution is mandatory for empty properties
    def __post_init__(self):    # Post Constructor
        self.z = self.y + 1

# ==========================================================================================================
# Test
# ==========================================================================================================

dtcls = DataClass(Complex(2, 3), 99)
print(dtcls.c.imaginary)
print(dtcls.c.real)
print(dtcls.x)
dtcls.x = 4

print("---------------------------------------------")

nsdtcls = NestedDataClass(DataClass(Complex(5, 6), 7), 8)
print(nsdtcls.dt.c.imaginary)
print(nsdtcls.dt.c.real)
print(nsdtcls.dt.x)
print(nsdtcls.y)
print(nsdtcls.z)