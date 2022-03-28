# Working with int -> string dictionaries

def to_list(dict):
    return [dict.get(i) for i in range(max(dict.keys()))]

def to_dict(list):
    result = {}
    for i in range(len(list)):
        if list[i] is not None:
            result[i] = list[i]
    return result

# These are just wrappers over common dictionary functions

def set(dict, key, value):
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
