# Try to figure out what these functions do,
# and what the types of the input and output are

def func1(z: dict[str, str]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    for x, y in z.items():
        result.append((x, y))
    return result

def func2(z: list[tuple[str, str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for x, y in z:
        result[x] = y
    return result

d: dict[str, str] = {"a": "b", "b": "c", "c": "d"}
e: list[tuple[str, str]] = func1(d)
f: dict[str, str] = func2(e)
assert d == f
