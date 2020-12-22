"""
Types of Methods in OOP
"""

class Student:
    
    school = "VIT"
    """
    There are 3 types of methods:
        - Class Methods: These methods are used to work on class variables.
                         In order to use the class methods you need to declare @classmethod 
                         decorator before the definition of the class method.   

        - Static Methods: These methods do not use class or instance variables, they are used 
                          for any internal functionality and are not required for fetching data.

        - Instance Methods: These mathods are used to work with instance variables.
             a. Accessor Methods: Those methods are responsible for fetching the values for variables, 
                                  are called Accessor Methods.(Example: get and set method)
             b. Mutator Methods:  

    
    """
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self,f):
        self.m1=m1

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print()



s1 = Student(34,45,67)
s2 = Student(89,45,34)

print(s1.avg())
print(s2.avg())
print(Student.info())

