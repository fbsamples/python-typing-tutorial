def split_strings_into_characters(strings: list[str]) -> list[list[str]]:
    """
    >>> split_into_characters(["PyCon", "Typing", "Workshop"])
    [['P', 'y', 'C', 'o', 'n'], ['T', 'y', 'p', 'i', 'n', 'g'], ['W', 'o', 'r', 'k', 's', 'h', 'o', 'p']]
    """
    result = []
    for string in strings:
        result.append(split_single_string_into_characters(string))
    return result

def split_single_string_into_characters(string: str) -> list[str]:
    """
    >>> split_into_characters("PyCon")
    ['P', 'y', 'C', 'o', 'n']
    """
    result = []
    for character in string:
        result.append(character)
    return result
