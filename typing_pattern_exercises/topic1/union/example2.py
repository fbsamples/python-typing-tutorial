# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# We mentioned in the talk that consuming values of union type often requires a
# case split. But there are also cases where the case split is not necessary.
# This example demonstrates those cases.

# Consider these two classes:


class Dog:
    def bark(self) -> None:
        print("Whoof! Whoof!")

    def play(self) -> None:
        print("Dog playing!")

    def chase(self, dog: Dog) -> None:
        print("Dog is chasing another dog!")


class Cat:
    def meow(self) -> None:
        print("Meow! Meow!")

    def play(self) -> None:
        print("Cat playing!")

    def chase(self, cat: Cat) -> None:
        print("Cat is chasing another cat!")


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

# TODO: Type-annotate the `make_sound` function. Is the case-split here
# necessary or not?


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

# TODO: Type-annotate the `make_sound` function. Is the case-split here
# necessary or not? Try removing the isinstance check and see if the type
# checker accepts the change.


# ------------------------------------------------------------------------------

# Question: Is it possible to type-annotate the following function with union
# type, without doing any case split in the function body? Why or why not?
def make_chase(pet0, pet1):
    pet0.chase(pet1)
    pet1.chase(pet0)


make_chase(Dog(), Dog())
make_chase(Cat(), Dog())
make_chase(Dog(), Cat())
make_chase(Cat(), Cat())
