# pyre-strict

# This example shows why it is not safe to have overriding method change the
# return type to be more general. Try run this file with a Python interpreter.


class Pet:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def clone(self) -> "Pet":
        return Pet(self.name)


class Dog(Pet):
    def clone(self) -> object:  # type: ignore
        return 42


def test(pet: Pet) -> None:
    clone = pet.clone()
    print(f"Name of cloned pet is {pet.name}")


test(Dog("Fido"))
