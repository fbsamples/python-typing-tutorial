# Step 1: Annotate this function.
def split_into_characters(s: str) -> list[str]:
    """
    >>> split_into_characters("PyCon")
    ['P', 'y', 'C', 'o', 'n']
    """
    return [character for character in s]

# Step 2: Annotate this function.
def strings_to_characters(strings: list[str]) -> list[list[str]]:
    """
    >>> strings_to_characters(["PyCon", "Typing", "Tutorial"])
    [['P', 'y', 'C', 'o', 'n'], ['T', 'y', 'p', 'i', 'n', 'g'], ['T', 'u', 't', 'o', 'r', 'i', 'a', 'l']]
    """
    return [split_into_characters(s) for s in strings]

# Step 3: Identify the bug present in one of these calls.
strings_to_characters(["PyCon", "Typing", "Tutorial"])
strings_to_characters(["PyCon", "Typing", "Tutorial", 2022, "is", "now"])

# Step 4: What do you think `Union[int, str]` means?
# (Hint: You've seen `Optional[str]`, which meant the type was either str or None. Can you see the similarity?)

# Step 5: What will be the type of the value you get from a list of type
# `List[Union[int, str]]`? Uncomment the following lines, use
# `reveal_type(<variable>)`, and run Pyre to see their types.

# xs = ["PyCon", "Typing", "Tutorial", 2022, "is", "now"]
# y = xs[0]
