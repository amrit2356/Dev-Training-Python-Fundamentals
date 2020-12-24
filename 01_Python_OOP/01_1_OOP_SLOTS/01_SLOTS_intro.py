"""
SLOTS -
    Speed of accessing the objects
    Memory consumed to create the objects.
"""
from pympler import asizeof

class Planet:
    def __init__(self,cities):
        self.cities = cities

earth  =  Planet(['Delhi','Oslo'])
print(earth.cities)
earth.rivers =('Thames','Siene')
print(earth.__dict__)


class SlottedPlanet:
    __slots__ = ['cities','__dict__']
    def __init__(self, cities):
        self.cities = cities

slottedearth = SlottedPlanet(['London','New York'])
slottedearth.random =10

print(slottedearth.__dict__)

print(asizeof.asizeof(earth))
print(asizeof.asizeof(slottedearth))
