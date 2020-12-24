"""
SLOTS -
    Speed of accessing the objects
    Memory consumed to create the objects.
"""


class Planet:
    def __init__(self,cities):
        self.cities = cities

earth  =  Planet(['Delhi','Oslo'])
print(earth)
print(earth.cities)



class SlottedPlanet:
    __slots__ = ['cities']
    def __init__(self, cities):
        self.cities = cities

slottedearth = SlottedPlanet(['London','New York'])
print(slottedearth)
print(slottedearth.cities)

earth.rivers =('Thames','Siene')

