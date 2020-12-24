"""
Implementation of Slots in Inheritance

"""
class B:
    __slots__ = ['first','second']

class D:
    pass
   
class MI(B,D):
    pass
    


obj = MI()    
obj.first =10
obj.second =100
obj.third = 120
print(obj.__dict__)

