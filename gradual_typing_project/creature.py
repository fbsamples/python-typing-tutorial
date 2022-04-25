# Basic creature types

import random
from typing import List


class Creature:
    def __init__(self, name):
        self.name = name

    def meet(self, other):
        pass

class Cat(Creature):
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.enemies = []

    def meet(self, other):
        if random.random() < 0.6:
            self.friends.append(other)
        else:
            self.enemies.append(other)
    
    def chase(self, other):
        if isinstance(other, Dog):
            raise Exception("Cats don't chase dogs.")
        print(f"{self.name} chases {other.name}!")
	

class Dog(Creature):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def meet(self, other):
        self.friends.append(other)
    
    def chase(self, other):
        print(f"{self.name} chases {other.name}!")
