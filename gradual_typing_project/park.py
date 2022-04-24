import random

from creature import Cat, Dog
from interact import play 

class Park:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def populate(self, input):
        for name in input['cats']:
            self.cats.append(Cat(name))
        for name in input['dogs']:
            self.dogs.append(Dog(name))

    def simulate_hour(self):
        # Some random animal interactions
        all_animals = self.cats + self.dogs
        for _ in range(random.randint(0, 5)):
            playmates = random.sample(all_animals, 2)
            play(playmates[0], playmates[1])
