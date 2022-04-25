# pyre-strict

# Try annotating the decorator below yourself. Try avoid union types and make
# your annotation as general as possible. For the sake of simplicity, let's
# simply ignore the issue with keyword arguments for now.


def my_decorator(original_func):
    def wrapped_func(x):
        print("Before calling original_func")
        result = original_func(x)
        print("After calling original_func")
        return result

    return wrapped_func


# Below are some tests to help you verify that the annotation above is working.
# The entire file should have no type errors if you did it correctly.


@my_decorator
def foo(x: int) -> int:
    return x + 1


foo(42)


@my_decorator
def bar(y: str) -> list[str]:
    return [y, y]


bar("Fluffy")


@my_decorator
def baz(z: bytes) -> bool:
    return len(z) <= 5


baz(b"Rover")


class Dog:
    def __init__(self, name: str) -> None:
        self.name = name


@my_decorator
def qux(name: str) -> Dog | None:
    return Dog(name) if name == "Fido" else None


qux("Fido")
