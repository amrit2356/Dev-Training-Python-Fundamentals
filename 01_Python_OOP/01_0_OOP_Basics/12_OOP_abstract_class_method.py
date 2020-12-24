"""
Implementation of Abstract class in python 
"""
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running...")


com = Laptop()
com.process()