"""
Constructors and Destructors in Python

"""


class Computer:
    """
    Everytime when we create an object, it will take memory space in the heap memory. 
    Size of the object is dependent on the number and type of data variables being used in the class.

       - "self" is a pointer which points to the object which is calling the variable or method.

    """
    def __init__(self):
        """
        This is the constructor, it is responsible to initialise all the instance variables when the object is 
        created during runtime of the program. There are 2 types of constructors in Python.
           - Default Constructor
           - Parameterised Constructor.
        """
        self.name = "Navin"
        self.age = 28
    
    def update(self):
        self.age = 30

    def compare(self,other):
        if(self.age ==other.age):
            return True
        else:
            return False
    def __del__(self):
        """
        This is the Destructor of python. It is executed once all the references to the object have been deleted.
        We generally don't need a destructor, because Python has a garbage collector, that handles memory management automatically.
        """
        print("This is a destructor, I destroyed all your objects, hahahaha !!!!")


if __name__ == "__main__":
    comp1 = Computer()
    comp2 = Computer()
    result = comp1.compare(comp2)
    print(comp1.name)
    print(comp1.age)