# NOTE: Skip down to the `PyCon` class for the first step.

class Talk:
  """
  >>> str(Talk("Python Typing Tutorial", 13))
  '1 PM - Python Typing Tutorial'
  """

  def __init__(self, title: str, hour: int) -> None:
      self.title = title
      self.hour = hour

  def __str__(self) -> str:
      am_pm_string = "AM" if self.hour < 12 else "PM"
      return f"{self.hour % 12} {am_pm_string} - {self.title}"



# Step 1: First, just read the following code to see if you can spot the bug(s).

# Step 2: Annotate the constructor and methods of this class.
class PyCon:
   """
   >>> pycon = PyCon("Salt Lake City", 2022)
   >>> pycon.add_talk(Talk("Securing Code with the Type System", 11))
   >>> pycon.add_talk(Talk("Python Typing Tutorial", 13))
   >>> print(pycon.calendar())
   2022 PyCon at Salt Lake City
   11 AM - Securing Code with the Type System
   1 PM - Python Typing Tutorial
   """

   # Step 3: There is an empty container assigned to an attribute. Do you know
   # how to annotate the attribute explicitly? (Hint: Use the same syntax as
   # for variables.)
   def __init__(self, location, year):
       self.location = location
       self.year = year
       self.talks = []

   def add_talk(self, talk):
       self.talks.append(talk)

   def calendar(self):
      """Return a string calendar of talks sorted by start time."""

       # Step 4: Nested functions need annotations too!
       def get_start_hour(talk):
           return talk.start_hour

       sorted_talks = sorted(self.talks, key=get_start_hour)
       talks = "\n".join(str(talk) for talk in sorted_talks)
       return f"{self.year} PyCon at {self.location}\n{talks}"


# Step 5: Identity the bug(s) in the following code (and any in the above code).
pycon = PyCon("Salt Lake City", 2022)
pycon.add_talk(Talk("Securing Code with the Type System", 11))
pycon.add_talk("Python Typing Tutorial")
pycon.add_talk([Talk("Cool Talk", 14), Talk("The Cool Talk Strikes Back", 15)])
print(pycon.calendar())
