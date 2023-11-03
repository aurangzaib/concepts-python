from dataclasses import dataclass
from enum import Enum

"""
==========================================================================================================
Note
==========================================================================================================

- An iterable class
- Properties can be of any type
- Properties are immutable contants

"""

# ==========================================================================================================
# Definition
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
# Test
# ==========================================================================================================

# No instance required for Enum classes
for company in Companies:
    print("{}:{}".format(company.name, company.value))
print(Companies.method())