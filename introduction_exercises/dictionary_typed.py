# Working with int -> string dictionaries

def set(dict: dict[int, str], key: int, value: str) -> None:
    dict[key] = value

def get(dict: dict[int, str], key: int) -> str | None:
    return dict.get(key)

def get_default(dict: dict[int, str], key: int, default: str) -> str:
    result = dict.get(key)
    if result is None:
        return default
    return result

def keys(dict: dict[int, str]) -> list[int]:
    return list(dict.keys())

def values(dict: dict[int, str]) -> list[str]:
    return list(dict.values())

def items(dict: dict[int, str]) -> list[tuple[int, str]]:
    return list(zip(keys(dict), values(dict)))

def to_list(dict: dict[int, str]) -> list[str | None]:
    max_key = max(keys(dict))
    result = [None] * max_key
    for key, value in items(dict):
        result[key] = value
    return result

def to_dict(list: list[str | None]) -> dict[int, str]:
    result = {}
    for i in range(len(list)):
        if list[i] is not None:
            result[i] = list[i]
    return result
