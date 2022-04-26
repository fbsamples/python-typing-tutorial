# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

from typing import TypeVar

# This exercise is about the scope of the typevar.

# Below we have 2 functions, `foo` and `bar`. They are defined with 2 different
# typevars, T and U.

T = TypeVar("T")


def foo(x: T) -> list[T]:
    ...


U = TypeVar("U")


def bar(y: U) -> U:
    ...


def test() -> int:
    return bar(42) + len(foo("abc"))


# TODO: Try changing the definition of `bar` such that it reuses the same
# typevar T as `foo`. How did your change affect type checking results?


# -----------------------------------------------------------------------------------------


# Now let's try something different. This time, we have an outer function
# `test` and an inner function `make_tuple_inner`. They are currently defined
# using 2 different typevars, T and U.


def test(x: T) -> tuple[int, int]:
    def make_tuple_inner(y: U, z: U) -> tuple[U, U]:
        return (y, z)

    return make_tuple_inner(0, 1)


# TODO: Try changing the definition of `make_tuple_inner` such that it reuses
# the same typevar T as `test`. How did your change affect type checking
# results?


# -----------------------------------------------------------------------------------------


# The general lesson here is that TypeVars can be freely reused across
# different functions, but they cannot be freely reused within the body of a
# single function.
