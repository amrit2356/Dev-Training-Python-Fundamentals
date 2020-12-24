"""
Implementation of Inheritance in Python
"""


class A:  # Super Class
    def feature1(self):
        print("print feature 1")
    
    def feature2(self):
        print("print feature 2")

class B(A): #Sub Class
    """
    class B is inheriting the features of class A
    """
    def feature3(self):
        print("print feature 3")
    
    def feature4(self):
        print("print feature 4")

class C(B):
    """
    class c is inheriting the features of class A and B
    """
    def feature5(self):
        print("print feature 5")
    
    def feature6(self):
        print("print feature 6")   



a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature3()
b1.feature4()


c1 = C()
c1.