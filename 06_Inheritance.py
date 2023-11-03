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
# Base Class
# ==========================================================================================================

class Students:
    def __init__(self, standard, grade, child,children=0, school="Hochschule Rosenheim"):
        self.school: str = school
        self.children: list = children
        self.standard: int = standard
        self.grade: float = grade
        self.child: int = child
    def set_child(self, child): self.children.append(child)
    def get_standard(self):     return self.standard
    def get_grade(self):        return self.grade
    def get_child(self):        return self.child
    def get_child_key(self):
        return self.child + 1

# ==========================================================================================================
# Inheritance
# ==========================================================================================================

class Student1(Students):
    def __init__(self, standard=1, grade=1, child=0):
        super().__init__(standard=standard, grade=grade, child=child)
    def get_child_key(self):
        return super().get_child_key()

# ==========================================================================================================
# Composition
# ==========================================================================================================

class Student2():
    def __init__(self, standard=1, grade=1, child=0):
        self.student = Students(standard=standard, grade=grade, child=child)
    def get_child_key(self):
        return self.student.child + 99

# ==========================================================================================================
# Composition with Dependency Injection
# ==========================================================================================================

class Student3():
    def __init__(self, s):
        self.student: Students = s
    def get_child_key(self):
        return self.student.child + 100

# ==========================================================================================================
# Test
# ==========================================================================================================

student  = Students(standard=6, grade=4.0, child=100)
student1 = Student1(standard=2, grade=2.0, child=2)
student2 = Student2(standard=5, grade=1.0, child=90)
student3 = Student3(student)

print(student1.standard)
print(student2.student.standard)
print(student3.student.standard)

print(student1.get_child_key())         # Method of Baseclass

print(student2.get_child_key())         # Method of Subclass
print(student2.student.get_child_key()) # Method of Baseclass

print(student3.get_child_key())         # Method of Subclass
print(student3.student.get_child_key()) # Method of Baseclass
