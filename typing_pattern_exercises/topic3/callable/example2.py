# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# This is a read-only example. It demonstrates some interesting behavior on the
# compatibility of Callable types.

from typing import Callable


class Pet:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Dog(Pet):
    def bark(self) -> None:
        print("Whoof! Whoof!")


# This function takes a callable that has `Pet` as the return type.
def test0(pet_factory: Callable[[], Pet]) -> None:
    ...


# This function is a callable that has `Dog` as the return type.
def make_fido() -> Dog:
    return Dog("Fido", 2)


# Question: should the type checker accept this call? Why or why not?
test0(make_fido)

# ------------------------------------------------------------------------------

# This function takes a callable that has `Pet` as the parameter type.
def test1(predicate: Callable[[Pet], bool]) -> None:
    ...


# This function is a callable that has `Dog` as the parameter type.
def is_dog_happy(dog: Dog) -> bool:
    return dog.age <= 2


# Question: should the type checker accept this call? Why or why not?
test1(is_dog_happy)

# ------------------------------------------------------------------------------


# This function takes a callable that constructs `Pet` from a string and an int.
def test2(pet_factory: Callable[[], Pet]) -> None:
    ...


# Question: should the type checker accept this call? Why or why not?
test2(Pet)
