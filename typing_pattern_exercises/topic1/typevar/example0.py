# pyre-strict

# Try annotating this function, using typevar
def make_pair(x, y):
    return (x, y)


# Here are some tests to help you verify that the annotation above is working.
# The entire file should have no type errors if you did it correctly.
def verify0(p: tuple[int, str]) -> None:
    ...


def verify1(p: tuple[bytes, list[float]]) -> None:
    ...


def verify2(p: tuple[bool, bool]) -> None:
    ...


def test_make_pair() -> None:
    verify0(make_pair(1, "foo"))
    verify1(make_pair(b"bar", [42.0]))
    verify2(make_pair(True, False))


# In the example above, how many type vars did you define?
