"""
SLOTS -
    Speed of accessing the objects
    Memory consumed to create the objects.
"""
import timeit
from pympler import asizeof

class ABC:
    def fn(self):
        self.third ="Universe"

class Slots():
    __slots__ = ('first','second','third')


obj = ABC()
obj.fn()
obj.first = "hello"
obj.second = "World"

print(obj.__dict__)

obj_slots = Slots()
def fn_slots():
    