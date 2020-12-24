"""
Implementation of Method Overriding in Python



"""

class A:
    def show(self):
        print("Displaying Value from Class A")


class B(A):
    def show(self):
        print("Displaying Value from Class B")


obj_test = B()
obj_test.show()