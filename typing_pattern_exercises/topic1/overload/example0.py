# pyre-strict

# The Python standard library has a built-in "round" function, which takes a
# float value and round it down. If no additional argument is provided, or if
# the ndigits argument is set to None, the input float will be round to the
# nearest integer. Otherwise, if ndigits is a integer, it specifies the number
# of decimal digits to keep, and the return value becomes a float. For example:

assert round(42.06) == 42
assert round(42.06, None) == 42
assert round(42.06, ndigits=None) == 42
assert round(42.06, 1) == 42.1
assert round(42.06, ndigits=1) == 42.1

# The exercise here is to try adding type annotation to this builtin functions.
# To avoid potential naming conflict, let's write our own wrapper of the
# `round` function and operate that instead.
# TODO: Type annotate the `my_round` function. The entire file should have no
# type errors if you did it correctly.


def my_round(value, ndigits=None):
    # An error suppression is needed here if fallback annotation is added.
    return round(value, ndigits)  # type: ignore


# Below are some tests to help you verify that the annotation above is working.
def verify0(r: int) -> None:
    ...


def verify1(r: float) -> None:
    ...


def test() -> None:
    verify0(my_round(42.06))
    verify0(my_round(42.06, None))
    verify0(my_round(42.06, ndigits=None))
    verify1(my_round(42.06, 1))
    verify1(my_round(42.06, ndigits=1))
