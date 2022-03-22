def get_name() -> str:
    return "YOUR NAME HERE"

def length(string: str) -> int:
    return len(string)

def contains_letter(string: str, letter: str) -> bool:
    return letter in string

def greet(name: str) -> str:
    return "Hello " + name + "!"

def introduction(name: str) -> str:
    return greet(name) + " Your name contains " + str(length(name)) + " letters. Does it contain the letter z: " + str(contains_letter(name, "z"))

introduction(get_name())
