import json

from shelter import Shelter


def print_stats(shelter):
    # Print counts.
    cats = str(len(shelter.cats))
    dogs = str(len(shelter.dogs)) 
    print("There are " + cats + " cats, " + dogs + " dogs.")

    # Print ratio.
    ratio = str(cats / dogs)
    print("Ratio of cats:dogs is " + ratio)


def main():
    shelter = Shelter()

    with open('data.json') as json_file:
        data = json.load(json_file)
        shelter.populate(data)

    # Simulate 8 hours of activity at the shelter
    for _ in range(8):
        stats = print_stats(shelter)
        print(stats)
        shelter.run()


if __name__ == "__main__":
    main()
