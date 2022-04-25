# Part 1 - Simple intro

def length(input):
    result = 0
    for _ in input:
        result += 1
    return result

# Part 2 - types to help catch a bug

def get_name():
    return "YOUR NAME HERE"

def greet(name):
    print("Hello " + name + "! Your name contains " + length(name) + " letters.")

greet(get_name())

# Part 3 - More bugs and bool type

def contains_letter(string, letter):
    return letter in string

def introduction(name):
    return greet(name) + " Does your name contain the letter z: " + contains_letter(name, "z")

introduction(get_name())
