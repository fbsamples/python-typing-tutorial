# pyre-strict

# We mentioned in the talk that consuming values of union type often requires a
# case split. But there are also cases where the case split is not necessary.
# This example demonstrates those cases.

# Consider these two classes:


class Dog:
    def bark(self) -> None:
        print("Whoof! Whoof!")

    def play(self) -> None:
        print("Dog playing!")

    def play_with(self, dog: Dog) -> None:
        print("Dog is playwith with another dog!")


class Cat:
    def meow(self) -> None:
        print("Meow! Meow!")

    def play(self) -> None:
        print("Cat playing!")

    def play_with(self, cat: Cat) -> None:
        print("Cat is playwith with another cat!")


# Now we have a function written like this:


def make_sound(pet):
    if isinstance(pet, Dog):
        pet.bark()
    elif isinstance(pet, Cat):
        pet.meow()
    else:
        raise RuntimeError


make_sound(Dog())
make_sound(Cat())

# Type-annotate the `make_sound` function. Is the case-split here necessary or
# not?


# ------------------------------------------------------------------------------

# Now consider the following function:


def make_play(pet):
    if isinstance(pet, Dog):
        pet.play()
    elif isinstance(pet, Cat):
        pet.play()
    else:
        raise RuntimeError


make_play(Dog())
make_play(Cat())

# Type-annotate the `make_sound` function. Is the case-split here necessary or
# not? Try removing the isinstance check and see if the type checker accepts
# the change.


# ------------------------------------------------------------------------------

# Can you type-annotate the following function with union type, without adding
# a case split in the function body? Why or why not?
def make_play_with(pet0, pet1):
    pet0.play_with(pet1)
    pet1.play_with(pet0)


make_play_with(Dog(), Dog())
make_play_with(Cat(), Dog())
make_play_with(Dog(), Cat())
make_play_with(Cat(), Cat())
