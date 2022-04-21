# Helper library for creature interactions

from typing import Any

from creature import Creature, Person, Cat, Dog

def are_enemies(creature_a, creature_b):
    return creature_a in creature_b.enemies or creature_b in creature_a.enemies 

def are_friends(creature_a, creature_b):
    if are_enemies(creature_a, creature_b):
        return False
    return creature_a in creature_b.friends or creature_b in creature_a.friends 

def play(creature_a, creature_b):
    if are_friends(creature_a, creature_b):
        print("{} and {} get along!".format(creature_a.name, creature_b.name))
    if are_enemies(creature_a, creature_b):
        print("{} and {} have a fight!".format(creature_a.name, creature_b.name))
    else:
        creature_a.meet(creature_b)
        creature_b.meet(creature_a)

def adopt(person, pet):
    pet.meet(person)
    if are_friends(person, pet) and all(
	are_friends(existing_pet, pet) for existing_pet in person.pets
    ):
        person.adopt(pet)
    
