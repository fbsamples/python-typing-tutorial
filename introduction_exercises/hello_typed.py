# Part 1 - Simple intro

def length(input: str) -> int:
    result = 0
    for _ in input:
        result += 1
    return result

# Part 2 - types to help catch a bug

def get_name() -> str:
    return "YOUR NAME HERE"

def greet(name: str) -> str:
    return "Hello " + name + "! Your name contains " + str(length(name)) + " letters."

# Part 3 - Another bug and bool type

def contains_letter(input: str, letter: str) -> bool:
    return letter in input

def introduction(name: str) -> str:
    return greet(name) + " Does your name contain the letter z: " + str(contains_letter(name, "z"))

introduction(get_name())
