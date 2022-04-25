import json
from park import Park
from typing import Optional


def get_cat_dog_ratio(park):
    cats = len(park.inside_park["cats"])
    dogs = len(park.inside_park["dogs"])
    print(f"There are {cats} cats and {dogs} dogs in the park.")
    if dogs > 0:
        return cats / dogs


def run(park):
    for hour in range(1, 9):
        print(f"Hour: {hour}")
        cat_dog_ratio = get_cat_dog_ratio(park)
        dog_cat_ratio = 1 / cat_dog_ratio
        print("Ratio of cats to dogs is" + cat_dog_ratio)
        print("Ratio of dogs to cats is " + dog_cat_ratio)
        park.simulate_hour()


if __name__ == "__main__":
    park = Park()
    with open('data.json') as json_file:
        data = json.load(json_file)
        park.populate(data)
    run(park)
