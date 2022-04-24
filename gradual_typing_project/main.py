import json

from park import Park


def get_ratio(park):
    cats = str(len(park.cats))
    print("There are " + cats + " cats.")
    dogs = str(len(park.dogs))
    print("There are " + dogs + " dogs.")
    return cats * 1.0 / dogs


def run(park):
    for hour in range(1, 9):
        ratio = get_ratio(park)
        print("Ratio at hour " + str(hour) + ": "  + ratio)
        park.simulate_hour()


if __name__ == "__main__":
    park = Park()
    with open('data.json') as json_file:
        data = json.load(json_file)
        park.populate(data)
    run(park)
