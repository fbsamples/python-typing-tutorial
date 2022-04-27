# Step 1: Rename the `hour` attribute in `Talk` to `start_hour`. Run Pyre and
# fix all the errors that it shows.
# (Note that if there is more than one error of the same kind in a function,
# Pyre only shows the first one.)

# NOTE: Go to the PyCon class for step 2.

class Talk:
  """
  >>> str(Talk("Python Typing Tutorial", 13))
  '1 PM - Python Typing Tutorial'
  """

  def __init__(self, title: str, hour: int) -> None:
      self.title = title
      self.start_hour = hour

  def __str__(self) -> str:
      am_pm_string = "AM" if self.start_hour < 12 else "PM"
      return f"{self.start_hour % 12} {am_pm_string} - {self.title}"

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

    def __init__(self, location: str, year: int) -> None:
        self.location = location
        self.year = year
        # Step 2: Change this `list` to a `set`. The way to represent a set of
        # Talks is `set[Talk]`.
        # Fix the errors that Pyre shows you.
        self.talks: set[Talk] = set()

    def add_talk(self, talk: Talk) -> None:
        self.talks.add(talk)

    def calendar(self) -> str:
        """Return a string calendar of talks sorted by start time."""

        def get_hour(talk: Talk) -> int:
            return talk.start_hour

        sorted_talks = sorted(self.talks, key=get_hour)
        talks = "\n".join(str(talk) for talk in sorted_talks)
        return f"{self.year} PyCon at {self.location}\n{talks}"


pycon = PyCon("Salt Lake City", 2022)
pycon.add_talk(Talk("Securing Code with the Type System", 11))
pycon.add_talk(Talk("Cool Talk", 14))
pycon.add_talk(Talk("Cool Talk II", 15))
print(pycon.calendar())
print(f"The first talk is {pycon.talks.pop()}")
