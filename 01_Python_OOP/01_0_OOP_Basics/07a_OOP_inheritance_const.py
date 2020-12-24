"""
Role of Constructors in  Inheritance and MRO(Method Resolution Operator)

Points to Remember:
   1. If the Super Class has a constructor and the Sub Class hasn't declared a constructor, 
      then the object of Sub Class will invoke the Super Class Constructor 
   
   2. If the Sub Class has the constructor, then the object of Sub Class will invoke the Sub Class's 
      constructor, irrespective of whether the Super Class has a constructor or not.
    
   3. if the Sub class constructor has the keyword 'super()__init()', then the subclass object will invoke 
      the Super Class's Constructor via the Sub Class's object.    
    
 Note: super() is a method, which is usde to call the super class methods from the derived class.
 Format: super().<Super Class method()> 
"""

class A:  # Super Class
    def __init__(self):
        print(" Im executing __init__ of A Class")

    def feature1(self):
        print("print feature 1")
    
    def feature2(self):
        print("print feature 2")

class B(): #Sub Class
    """
    class B is inheriting the features of class A
    """
    
    def __init__(self):
        print(" Im executing __init__ of B Class")


    def feature3(self):
        print("print feature 3")
    
    def feature4(self):
        print("print feature 4")

class C(A,B):
    """"
    Method Resolution Order(MRO):
        Whenever, multiple inheritance is being invoked, if we call the constructor of the sub class
    the object will invoke the first class's constructor. This is called Method Resolution Order. Here,
    A takes higher precedence over B, and therefore, A's constructor was invoked.
    
    """"
    def __init__(self):
        super().__init__()
        print(" Im executing __init__ of C Class")




c1 = C()
