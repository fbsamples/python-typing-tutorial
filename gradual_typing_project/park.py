# Simulate creature activity in the park

import random
from pet import Cat, Dog
from interact import play


class Park:
    def __init__(self):
        self.inside_park = {
            "cats": [],
            "dogs": [],
        }
        self.outside_park = {
            "cats": [],
            "dogs": [],
        }

    def populate(self, input):
        for creature in input:
            name = creature["name"]
            if creature["type"] == "cat":
                if creature["in_park"]:
                    self.inside_park["cats"].append(Cat(name))
                else:
                    self.outside_park["cats"].append(Cat(name))
            elif creature["type"] == "dog":
                if creature["in_park"]:
                    self.inside_park["dogs"].append(Dog(name))
                else:
                    self.outside_park["dogs"].append(Dog(name))
            else:
                raise Exception("Invalid creature type provided.")

    def simulate_leave_and_enter(self, creature_key):
        inside_park = self.inside_park[creature_key]
        random.shuffle(inside_park)
        outside_park = self.outside_park[creature_key]
        random.shuffle(outside_park)

        number_leaving = random.randint(0, len(inside_park) // 2)
        number_arriving = random.randint(0, len(outside_park) // 2)
        self.inside_park[creature_key] = (
            inside_park[number_leaving:] + outside_park[:number_arriving]
        )
        self.outside_park[creature_key] = (
            inside_park[:number_leaving] + outside_park[number_arriving:]
        )

    def simulate_hour(self):
        # Random animal interactions
        creatures_inside_park = self.inside_park["cats"] + self.inside_park["dogs"]
        if len(creatures_inside_park) > 1:
            for _ in range(random.randint(1, 5)):
                playmates = random.sample(creatures_inside_park, 2)
                play(playmates[0], playmates[1])

        # Random animals leave
        self.simulate_leave_and_enter("cats")
        self.simulate_leave_and_enter("dogs")
