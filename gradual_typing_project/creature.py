# Basic creature types

import random

from typing import List

class Creature:
    def __init__(self, name):
        self.name = name

    def meet(self, other):
        pass


class Person(Creature):
    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt(self, pet):
        self.pets.append(pet)


class Cat(Creature):
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.enemies = []

    def make_friend(self, friend):
        self.friends.append(friend)

    def make_enemy(self, enemy):
        self.enemies.append(enemy)

    def meet(self, other):
        if random.random() < 0.5:
            self.make_friend(other)
        else:
            self.make_enemy(other)
	

class Dog(Creature):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def make_friend(self, friend):
        self.friends.append(friend)

    def meet(self, other):
        self.make_friend(other)
