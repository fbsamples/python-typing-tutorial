# pyre-strict

# Here is a (rather naive) implementation of a "filter" function. What it does
# is to take a predicate, which is supposed to be a unary function that returns
# a boolean value, along with a bunch of elements, and returns a list
# containing all elements on which the predicate returns true.


def my_filter(predicate, elements):
    results = []
    for element in elements:
        if predicate(element):
            results.append(element)
    return results


# A number of concrete pieces of logic can be implemented with it. For example,
# this is a function that takes a collection of numbers, and drop all the ones
# in it that’s larger than certain threshold:

from typing import Iterable


def drop_large_numbers(numbers: Iterable[int], limit: int) -> list[int]:
    return my_filter(lambda x: x <= limit, numbers)


# This is a function that takes a directory and returns all Python source files
# in that directory:

import pathlib


def get_python_files_in_directory(directory: pathlib.Path) -> list[pathlib.Path]:
    return my_filter(lambda p: p.suffix == ".py", directory.iterdir())


# And this is a function that takes a collection of employees and return all
# the ones that have remained employed after 10 years:


class Employee:
    def __init__(self, tenure: int) -> None:
        self.tenure: int = tenure


def get_senior_employees(employees: Iterable[Employee]) -> list[Employee]:
    return my_filter(lambda employee: employee.tenure >= 10, employees)


# TODO: Please fill in the type annotation of the `my_filter` function, so all
# of its callsites in this file could type check. Avoid using union type in
# your annotation, if possible.
