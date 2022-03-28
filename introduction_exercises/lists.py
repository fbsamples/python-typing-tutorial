def split_single_string_into_characters(string):
    """
    >>> split_into_characters("PyCon")
    ['P', 'y', 'C', 'o', 'n']
    """
    return [character for character in string]

def split_strings_into_characters(strings):
    """
    >>> split_into_characters(["PyCon", "Typing", "Workshop"])
    [['P', 'y', 'C', 'o', 'n'], ['T', 'y', 'p', 'i', 'n', 'g'], ['W', 'o', 'r', 'k', 's', 'h', 'o', 'p']]
    """
    return [split_single_string_into_characters(string) for string in strings]

def ints_to_repeated_strings(ints):
    """
    >>> ints_to_repeated_strings([1, 2, 3, 0, -1, 5, -100])
    ["1", "22", "333", None, None, "55555", None]
    """
    return [str(i) * i if i > 0 else None for i in ints]
