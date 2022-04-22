import json

from shelter import Shelter


def get_ratio(shelter):
    cats = str(len(shelter.cats))
    print("There are " + cats + " cats.")
    dogs = str(len(shelter.dogs))
    print("There are " + dogs + " dogs.")
    return cats * 1.0 / dogs


def run(shelter):
    for hour in range(1, 9):
        ratio = get_ratio(shelter)
        print("Ratio at hour " + str(hour) + ": "  + ratio)
        shelter.simulate_hour()


if __name__ == "__main__":
    shelter = Shelter()
    with open('data.json') as json_file:
        data = json.load(json_file)
        shelter.populate(data)
    run(shelter)
