# Helper library for creature interactions
 
from creature import Creature, Cat, Dog
from typing import Any


def are_enemies(a, b):
    return a in b.enemies or b in a.enemies

def are_friends(a, b):
    return a in b.friends and b in a.friends

def play(a, b):
    if are_friends(a, b):
        print(f"{a.name} and {b.name} get along!")
    elif are_enemies(a, b):
        print(f"{a.name} and {b.name} have a fight!")
        a.chase(b)
        b.chase(a)
    else:
        a.meet(b)
        b.meet(a)
    
