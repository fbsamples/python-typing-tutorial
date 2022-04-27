# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# A (hypothetical) Python developer is having some troubles typing his
# code that are related to SQL. Here is the code:

from datetime import datetime
from typing import Union

SQLTypes = Union[None, str, bytes, int, float, bool, datetime]


def process_row(row: dict[str, SQLTypes]) -> None:
    print(row)


def test() -> None:
    fred: dict[str, int | str | None] = {"age": 42, "name": "Fred", "pet": None}
    process_row(row=fred)


# The developer was confused about the type error. He understands that the
# declared row does not fully conform to the SQLTypes typing, but it's
# effectively a subset. Why is this an incompatible type?

# TODO: Try to change one type annotation in this file to resolve the type error.
