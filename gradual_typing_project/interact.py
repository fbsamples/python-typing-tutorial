# Helper library for creature interactions
 
from typing import Any

from creature import Creature, Person, Cat, Dog

def are_enemies(a, b):
    return a in b.enemies or b in a.enemies 

def are_friends(a, b):
    return a in b.friends or b in a.friends 

def play(a, b):
    if are_friends(a, b):
        print("{} and {} get along!".format(a.name, b.name))
    if are_enemies(a, b):
        print("{} and {} have a fight!".format(a.name, b.name))
    else:
        a.meet(b)
        b.meet(a)

def adopt(person, pet):
    pet.meet(person)
    if are_friends(person, pet):
        person.adopt(pet)
    
