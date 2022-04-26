# pyre-strict

# This example shows why it is not safe to have overriding method change the
# parameter type to be more specific. Try run this file with a Python
# interpreter (e.g. `python3 example2.py`).


class Pet:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def likes(self, other: "Pet") -> bool:
        return True


class Dog(Pet):
    pass


class Cat(Pet):
    def is_fluffy(self) -> bool:
        return self.name == "Fluffy"

    def likes(self, other: "Cat") -> bool:  # type: ignore
        return other.is_fluffy()


def likes_fido(pet: Pet) -> bool:
    return pet.likes(Dog("Fido"))


print(likes_fido(Cat("Fluffy")))
