from dataclasses import dataclass, field

# ==========================================================================================================
# Definition
# ==========================================================================================================

class C0:
    def __init__(self):
        self.a: int = 1

@dataclass
class C1:
    b: int = 2

@dataclass(frozen=True)
class C2:
    c: int = 3

@dataclass(frozen=True)
class C3:
    c0: C0 = C0()
    c1: C1 = field(default_factory=C1)
    c2: C2 = C2()
    d: int = 4

# ==========================================================================================================
# Test
# ==========================================================================================================

c3 = C3()
c3.c0.a = 99 # allowed
c3.c1.b = 99 # allowed
c3.c2.c = 99 # NOT allowed
c3.d    = 99 # NOT allowed

