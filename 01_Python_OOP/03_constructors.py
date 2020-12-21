"""
Constructors and Self Constructors in Python

"""


class Computer:
    """
    Everytime when we create an object, it will take memory space in the heap memory. 
    Size of the object is dependent on the number and type of data variables being used in the class.

       - "self" is a pointer which points to the object which is calling the variable or method.

    """
    def __init__(self):
        self.name = "Navin"
        self.age = 28
    
    def update(self):
        self.age = 30

    def compare(self,other):
        if(self.age ==other.age):
            return True
        else:
            return False


if __name__ == "__main__":
    comp1 = Computer()
    comp2 = Computer()
    result = c1.update(c2)
    print(comp1.name)
    print(comp1.age)