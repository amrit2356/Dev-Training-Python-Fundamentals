"""
Implementation of Method Overloading in Python
"""

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None amd c!=None:
            s=a+b+c
        elif(a! = 

s1 = Student(58,69)
print(s1.sum(5,9))
