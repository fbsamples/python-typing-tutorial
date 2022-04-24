# pyre-strict

# This exercise is about basic object-oriented programming in Python.
# Let's define a simple class hierarchy:


class Pet:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def play_with(self, other: "Pet") -> None:
        print(f"{self.name} is playing with {other.name}")


# Subclasses of Pet "inherits" all the attributes and methods in the parent
# class. So any Dog will also have a name and a play_with method. What’s more,
# Dog can also add new attributes or new methods that do not exist in the Pet
# class.
class Dog(Pet):
    def bark(self) -> None:
        print("Whoof! Whoof!")


#  Another thing that may happen in subclass is that you can define attributes
#  or methods that has the same name as the attributes or methods in the parent
#  class. Doing this will make the definition in the child class "override" the
#  corresponding definition in the parent. The end result of the overriding is
#  that the `Cat` objects and Pet objects may share the same `play_with`
#  interface, but when you invoke that interface, they will behave differently.
class Cat(Pet):
    def play_with(self, other: Pet) -> None:
        print(f"{self.name} does not want to play with {other.name}")


# Type-annotate the following functions without using union type. The function
# should accepts both kinds of pets, but nothing else.
def befriend(pet0, pet1):
    pet0.play_with(pet1)
    pet1.play_with(pet0)


# Below are some tests to help you verify that the annotation above is working.
# The `test` function should have no type errors if you did it correctly.


def test() -> None:
    befriend(Dog("Fido"), Dog("Rover"))
    befriend(Dog("Fido"), Cat("Fluffy"))
    befriend(Cat("Fluffy"), Dog("Fido"))
    befriend(Cat("Fluffy"), Cat("Silky"))


# -------------------------------------------------------------------------------


# Here's another class that tries to extend Pet. The type checker complains
# about it. Can you spot why?


class Duck(Pet):
    def play_with(self) -> None:
        print(f"{self.name} is playing by itself")


# Trying executing this file with the Python interpreter to get a sense of why
# the definition of `Duck` is problematic.
befriend(Dog("Fido"), Duck("Donald"))
