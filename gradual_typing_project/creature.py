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
        if random.random() < 0.5:
            self.friends.append(other)
        else:
            self.enemies.append(other)
	

class Dog(Creature):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def meet(self, other):
        self.friends.append(other)
