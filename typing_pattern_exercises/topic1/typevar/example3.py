# pyre-strict

# TypeVars can also take a "bound" argument. Suppose we have a class hierachy like this:


class Pet:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Pet):
    pass


class Cat(Pet):
    pass


# And we have a function that is supposed to operate on any subclasses of Pet:


def make_cute(pet):
    original_name = pet.name
    new_name = f"Cute {original_name}"
    pet.name = new_name
    return pet


# It's apparent that the function has the same parameter and return type, so we
# might want to use a type var. Try annotating the function above with a simple
# typevar and see what happens -- why do you think the type checker complains?

# Now, add a "bound" argument to your typevar like this:
# T = TypeVar("T", bound=Pet)
# This basically tells the type checker that within the function body, T is
# guaranteed to be a subclass of Pet, which makes it possible for us to access
# its `name` field within the function. Such trick is often useful, for
# example, when you use the builder pattern.
