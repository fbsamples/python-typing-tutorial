# Working with int -> string dictionaries

def set(dict, key, value) -> None:
    dict[key] = value

def get(dict, key):
    return dict.get(key)

def get_default(dict, key, default):
    result = dict.get(key)
    if result is None:
        return default
    return result

def keys(dict):
    return list(dict.keys())

def values(dict):
    return list(dict.values())

def items(dict):
    return list(zip(keys(dict), values(dict)))

def to_list(dict):
    max_key = max(keys(dict))
    result = [None] * max_key
    for key, value in items(dict):
        result[key] = value
    return result

def to_dict(list):
    result = {}
    for i in range(len(list)):
        if list[i] is not None:
            result[i] = list[i]
    return result
