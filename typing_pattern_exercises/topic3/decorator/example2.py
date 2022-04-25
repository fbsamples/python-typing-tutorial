# pyre-strict

# This exercise will be an extension of the test framework exercise we had in
# the callback protocol section. Please go through that exercise first before
# attempting this one.

# One of the drawback of our framework there was that every individual test
# case has to declare a boolean flag and ignore that flag in its body, which is
# annoying. We would like to lift that restriction here. Plus, we would also
# like our test framework to gather some basic statistics in the end, telling
# us how many tests it runs and how many of them have passed/failed.

# The key idea here is to use a decorator to reshape simple None-returning
# nullary functions into functions that take useful arguments and produce
# useful returns:

from dataclasses import dataclass


@dataclass(frozen=True)
class TestResult:
    pass_count: int
    fail_count: int


def test_case(func):
    def wrapper(fail_fast):
        try:
            func()
            return TestResult(pass_count=1, fail_count=0)
        except Exception:
            return TestResult(pass_count=0, fail_count=1)

    return wrapper


# Now, we can just write normal None-returning nullary functions as test cases,
# provided that they are decorated with the `test_case` decorator. For example:


@test_case
def simple_test_case_passes() -> None:
    assert 1 + 2 == 3
    assert "Fido" != "Fluffy"


@test_case
def simple_test_case_fails() -> None:
    assert len("Fido") == 3


# Now let's define a "test suite", which again is a combination of test cases,
# grouped together so it just looks like one single test case:


def create_test_suite(test_cases):
    def combined_test_case(fail_fast):
        results = []
        for test_case in test_cases:
            result = test_case(fail_fast=fail_fast)
            results.append(result)
            if fail_fast and result.fail_count > 0:
                break
        return TestResult(
            pass_count=sum(result.pass_count for result in results),
            fail_count=sum(result.fail_count for result in results),
        )

    return combined_test_case


# Here is the top-level "driver" API to run a given test case:


def run_test(test_case, fail_fast=False):
    result = test_case(fail_fast=fail_fast)
    print(
        f"Ran {result.pass_count + result.fail_count} tests."
        f"Had {result.fail_count} failures."
    )


# Please add type annotations to the `test_case` decorator, the
# `create_test_suite` function, and the `run_test` function. Below are code
# that helps verify whether your annotations work or not. You can also try
# running them for real by invoking Python interpreter on this file.


@test_case
def test_case0() -> None:
    pass


@test_case
def test_case1() -> None:
    assert False


@test_case
def test_case2() -> None:
    assert False


@test_case
def test_case3() -> None:
    pass


def test_all() -> None:
    run_test(test_case0)
    run_test(test_case1, fail_fast=True)
    run_test(create_test_suite([test_case0, test_case1]))
    run_test(
        create_test_suite((test_case0, create_test_suite([test_case1, test_case2])))
    )
    run_test(
        create_test_suite(
            (
                create_test_suite([test_case0, test_case1]),
                create_test_suite((test_case2,)),
            )
        ),
        fail_fast=True,
    )


test_all()
