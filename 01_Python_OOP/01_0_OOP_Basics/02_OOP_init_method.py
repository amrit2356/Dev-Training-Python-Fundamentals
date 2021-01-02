"""
init method() in Python:

"""

class Computer:
    """
    __init__ method is a function which is used to initialise variables.
    """
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        

    def config(self):
       return print("Config: ", self.cpu,self.ram)
    
if __name__ == "__main__":
    com1 = Computer('i5',16)
    com1.config()