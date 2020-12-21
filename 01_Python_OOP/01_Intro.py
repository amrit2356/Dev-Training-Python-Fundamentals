"""
Introduction to Object Oriented Programming using Python
    Class - Design or Blueprint of objects
    Object - Instance of the class.

"""

class Computer:
    """
    A class contains 2 sets of properties:
        - Attributes(Variables)
        - Behaviour(Methods/ Functions)
    """
    def config(self):
       return print("i5 ,16gb,1TB")

if __name__ == "__main__":
    comp1 = Computer()
    comp2 = Computer()
    
    #Method 1 of using an object to call a function 
    Computer.config(comp1)

    # Method 2 of using an object to call a function
    comp2.config()
    
    

