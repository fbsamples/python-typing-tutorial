# Step 1: Annotate `get_name`.
# Step 2: Annotate `greet`.
# Step 3: Identify the bug in `greet`.

def num_vowels(s: str) -> int:
   result = 0
   for letter in s:
       if letter in "aeiouAEIOU":
           result += 1
   return result

def get_name():
   return "YOUR NAME HERE"

def greet(name):
   print("Hello " + name + "! Your name contains " + num_vowels(name) + " vowels.")

# Step 4: Is this call necessary? Does Pyre catch the above bug even without
# this line?
greet(get_name())
