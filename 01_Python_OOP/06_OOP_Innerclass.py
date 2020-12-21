"""
Inner Class in Python
"""

class Student:
    """
    Inner class is a concept where we declare a class inside a class.
    so to use this class:
        - You can create the object of the inner class inside the outer class.
        - You can create object of inner class outside the outer class provided you use the outer
          class constructor to call it.
    """
    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu  = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('Navin',2)
s2 = Student('Jenny', 3)


s1.show()

print(s1.lap.brand)

lap1 = Student.Laptop()
lap1.show()
