# pyre-strict

# Try annotating this function, using typevar
def flatten_list(inputs):
    return [x for y in inputs for x in y]


# Here are some tests to help you verify that the annotation above is working.
# The entire file should have no type errors if you did it correctly.
def verify0(l: list[int]) -> None:
    ...


def verify1(l: list[str]) -> None:
    ...


def verify2(l: list[list[int]]) -> None:
    ...


def test_flatten_list() -> None:
    verify0(flatten_list([[1], [], [2, 3]]))
    verify1(flatten_list([["foo", "bar"], ["baz"]]))
    verify2(flatten_list([[[0], [1]], [[2, 3]]]))
