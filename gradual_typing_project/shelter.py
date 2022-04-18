# Basic shelter type

import random

from creature import Cat, Dog, Person
from interact import adopt, play 

class Shelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.people = []

    def populate(self, input):
        for name in input['cats']:
            self.cats.append(Cat(name))
        for name in input['dogs']:
            self.dogs.append(Dog(name))
        for name in input['people']:
            self.people.append(Person(name))

    def run(self):
        # Some random animal interactions
        all_animals = self.cats + self.dogs
        for _ in range(random.randint(0, 5)):
            play(random.choice(all_animals), random.choice(all_animals))

        # Some attempted adoptions
        for person in self.people:
            for _ in range(random.randint(0, 3)):
                adopt(person, random.choice(all_animals))

