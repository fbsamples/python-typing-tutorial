# Step 1: Annotate this function.
def split_into_characters(s):
  """
  >>> split_into_characters("PyCon")
  ['P', 'y', 'C', 'o', 'n']
  """
  return [character for character in s]

# Step 2: Annotate this function.
def strings_to_characters(strings):
  """
  >>> strings_to_characters(["PyCon", "Typing", "Tutorial"])
  [['P', 'y', 'C', 'o', 'n'], ['T', 'y', 'p', 'i', 'n', 'g'], ['T', 'u', 't', 'o', 'r', 'i', 'a', 'l']]
  """
  return [split_into_characters(s) for s in strings]

# Step 3: Identify the bug present in one of these calls.
strings_to_characters(["PyCon", "Typing", "Tutorial"])
strings_to_characters(["PyCon", "Typing", "Tutorial", 2022, "is", "now"])
