"""
Implementation of Polymorphism - DuckTyping in Python
"""

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Myeditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    
    def code(self,ide):
        ide.execute()

#ide = Pycharm()
ide  = Myeditor()

lap1 = Laptop()
lap1.code(ide)