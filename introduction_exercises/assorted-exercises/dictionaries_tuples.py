# Try to figure out what these functions do,
# and what the types of the input and output are

def func1(z):
    result = []
    for x, y in z.items():
        result.append((x, y))
    return result

def func2(z):
    result = {}
    for x, y in z:
        result[x] = y
    return result

d = {"a": "b", "b": "c", "c": "d"}
e = func1(d)
f = func2(e)
assert d == f
