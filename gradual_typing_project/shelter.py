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

    def simulate_hour(self):
        # Some random animal interactions
        all_animals = self.cats + self.dogs
        for _ in range(random.randint(0, 5)):
            playmates = random.sample(all_animals, 2)
            play(playmates[0], playmates[1])

        # Some attempted adoptions
        for person in self.people:
            for _ in range(random.randint(0, 3)):
                adopt(person, random.choice(all_animals))

