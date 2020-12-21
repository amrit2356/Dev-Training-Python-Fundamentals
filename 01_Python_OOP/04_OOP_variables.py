"""
Types of Variables in OOP

"""


class Car:
    """
    There are 2 types of Variables:
        - Instance Variables -> variables used for the instantiation of class and declared inside init() method
        - Class Variables(static variables) -> variables which are used inside the class but are not declared inside 
                                               init() method.
    
    namespace: it is an area where you create and store the object/ variable
        - Instance Namespace: the place where we declare instance varaibles(init method)
        - Class Namespace: the place where the class variables are declared.

    Note: using objects for the same set of instance variables, you can store different values. However, if you change 
    the class variable, it will be reflected in all the objects, (irrespective of the values held in the instance variables). 

    """
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"
    


c1 = Car()
c2 = Car()

c1.mil = 8
c2.wheels =7

print(c1.com, c1.mil, c2.wheels)
print(c2.com, c2.mil, c2.wheels)
