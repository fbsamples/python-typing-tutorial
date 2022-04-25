# Step 1: Annotate the function signature of `num_vowels`: add a type
# annotation for the parameter `input` and the return type.

# Step 2: Identify which of the two callers is calling this function
# incorrectly. (You do not need to fix the bug.)

def num_vowels(s):
   result = 0
   for letter in s:
       if letter in "aeiouAEIOU":
           result += 1
   return result


num_vowels("PyCon is cool")
num_vowels(["PyCon", "is", "cool"])
