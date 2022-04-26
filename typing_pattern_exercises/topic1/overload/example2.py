# pyre-ignore-all-errors

# This is a read-only exercise.

from typing import overload

# Using overloads to annotate functions is sometimes unavoidable because the
# function comes from a third party library you do not control, and you are
# just writing type stubs for it.
# But if you do have full control over the source code and are able to do some
# refactoring, there are ways to avoid the complexity and the hassle of
# overloads altogether.

# One thing to realize is that overloads are necessary only when you want
# different function signatures to share the same name. If there's no name
# sharing, no overload needed. Hence the easiest way to avoid overloads is to
# break the overloaded name into separate functions. Take the `receive_data`
# example we had in the talk:


@overload
def receive_data() -> bytes:
    pass


@overload
def receive_data(encoding: None) -> bytes:
    pass


@overload
def receive_data(encoding: str) -> str:
    pass


def receive_data(encoding: str | None = None) -> bytes | str:
    ...


# Instead of having one function that may return either a bytes or a string,
# write two different functions instead:


def receive_bytes_data() -> bytes:
    ...


def receive_str_data(encoding: str) -> str:
    ...


# Downstream code will be able to choose which one to use on their side based
# on the name of the function, not on the number or the types of the arguments.
# No overload is required at all.

# The same thing can be done in other examples. Try thinking of a way to break
# the `round` function and the `run` function we wrote in other exercises.
