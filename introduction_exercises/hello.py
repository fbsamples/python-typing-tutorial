def get_name():
    return "YOUR NAME HERE"

def length(string):
    return len(string)

def contains_letter(string, letter):
    return letter in string

def greet(name):
    return "Hello " + name + "!"

def introduction(name):
    return greet(name) + " Your name contains " + str(length(name)) + " letters. Does it contain the letter z: " + str(contains_letter(name, "z"))

introduction(get_name())
