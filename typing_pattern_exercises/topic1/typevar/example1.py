# pyre-strict

# TODO: Try annotating this function, using typevar
# Hint: here are some example behaviors of this function:
# flatten_list([[1], [], [2, 3]]) == [1, 2, 3]
# flatten_list([["foo", "bar"], ["baz"]]) == ["foo", "bar", "baz"]
# flatten_list([[[0], [1]], [[2, 3]]]) == [[0, 1], [2, 3]]
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
