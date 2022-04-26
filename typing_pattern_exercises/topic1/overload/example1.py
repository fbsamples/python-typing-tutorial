# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# PEP 586 introduces the notion of "literal type" (see
# https://docs.python.org/3/library/typing.html#typing.Literal). A literal type
# is a type that can be used to indicate to type checker that the corresponding
# variable can only take certain (int, boolean, string, or enum) values. For
# example:

from typing import Literal


def only_take_one(x: Literal[1]) -> None:
    ...


only_take_one(1)  # OK
# only_take_one(2) will error, since only the integer literal 1 has the type
# `Literal[1]`.


def only_take_true(x: Literal[True]) -> None:
    ...


only_take_true(True)  # OK
# only_take_one(False) will error, due to same reason before.


# Given the information above, let's try adding type annotation to the
# following function. It's a simple wrapper around `subprocess.run`. The idea
# is that we have a flag to control whether the return code or the stdout of
# the subprocess invocation should be returned.
# TODO: Type annotate the `run` function. The entire file should have no type
# errors if you did it correctly.

import subprocess


def run(command, keep_stdout=False):
    # https://docs.python.org/3/library/subprocess.html#subprocess.run
    # The code only works on Python 3.7+
    result = subprocess.run(
        command.split(),
        text=True,
        capture_output=keep_stdout,
    )
    if keep_stdout:
        return result.stdout
    else:
        return result.returncode


# Below are some tests to help you verify that the annotation above is working.
def verify0(r: int) -> None:
    ...


def verify1(r: str) -> None:
    ...


def test() -> None:
    verify0(run("touch foo.py"))
    verify0(run("touch foo.py", keep_stdout=False))
    verify1(run("cat foo.py", keep_stdout=True))
