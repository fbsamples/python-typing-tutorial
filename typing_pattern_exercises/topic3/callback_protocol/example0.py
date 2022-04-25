# pyre-strict

# In this exercise, we are going to craft a simple test framework.

# An individual "test case" is a function that returns None. If the function
# returns normally, we consider the test passed. Otherwise, we consider it
# failed. Test cases are required to take one boolean flag as argument by our
# framework, but the body of the test case should ignore that flag.


def simple_test_case_passes(fail_fast: bool) -> None:
    assert 1 + 2 == 3
    assert "Fido" != "Fluffy"


def simple_test_case_fails(fail_fast: bool) -> None:
    assert len("Fido") == 3


# A "test suite" is a combination of test cases, grouped together so it just
# looks like one single test case. For test suites, the `fail_fast` boolean
# flag is meaningful: if any test case within the suite fails, we abort the
# entire test suite if `fail_fast` is set to True, but keep going if
# `fail_fast` is set to False.


def create_test_suite(test_cases):
    def combined_test_case(fail_fast):
        for test_case in test_cases:
            try:
                test_case(fail_fast=fail_fast)
            except Exception:
                if fail_fast:
                    break

    return combined_test_case


# We also provide an API to run a given test case, while at the same time
# allowing the user to control if they want the tests to fail fast:


def run_test(test_case, fail_fast=False):
    return test_case(fail_fast=fail_fast)


# Please add type annotations to the `create_test_suite` function and the
# `run_test` function. Below are code that helps verify whether your
# annotations work or not.


def test_case0(fail_fast: bool) -> None:
    ...


def test_case1(fail_fast: bool) -> None:
    ...


def test_case2(fail_fast: bool) -> None:
    ...


def test_case3(fail_fast: bool) -> None:
    ...


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
