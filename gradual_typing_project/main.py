import json

from shelter import Shelter


def print_stats(shelter):
    cats = str(len(shelter.cats))
    dogs = str(len(shelter.dogs)) 
    ratio = str(cats / dogs)
    print("There are " + cats + " cats, " + dogs + " dogs. Ratio: " + ratio)


def run(shelter):
    for hour in range(1, 9):
        stats = print_stats(shelter)
        print("Stats at hour " + str(hour) + ": "  + stats)
        shelter.simulate_hour()


if __name__ == "__main__":
    shelter = Shelter()
    with open('data.json') as json_file:
        data = json.load(json_file)
        shelter.populate(data)
    run(shelter)
