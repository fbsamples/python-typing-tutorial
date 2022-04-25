# pyre-strict

# Consider the following class hierarchy:


class Pet:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Dog(Pet):
    def bark(self) -> None:
        print("Whoof! Whoof!")


class Cat(Pet):
    def meow(self) -> None:
        print("Meow! Meow!")


# Also consider a function that takes a list of Pet as argument. The body of
# this function is currently kept empty. You will be asked to fill it in later.


def process_pets(pets: list[Pet]) -> None:
    raise NotImplementedError


# And finally, let's have a test function that invokes the `process_pets` function:


def test() -> None:
    my_cats = [Cat("Fluffy")]
    process_pets(my_cats)
    for cat in my_cats:
        cat.meow()


test()


# Notice that the type checker is not OK with this file: it reports a type error.
# Look at the type error and see if you can figure out the rationale.
# Also consider what would happen if the type checker accepts the code as-is:
# can you think of a type-safe thing that the `process_pets()` function may do,
# which can lead to a crash in the `test()` function? Trying replacing the body
# of `process_pets()` with what you came up with, and run this file with the
# Python interpreter to verify your thoughts.
