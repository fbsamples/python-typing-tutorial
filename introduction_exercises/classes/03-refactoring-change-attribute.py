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
      self.hour = hour

  def __str__(self) -> str:
      am_pm_string = "AM" if self.hour < 12 else "PM"
      return f"{self.hour % 12} {am_pm_string} - {self.title}"

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
        # Quick reminder that an empty set in Python is `set()` (not `{}`,
        # which is an empty dictionary).
        # Fix the errors that Pyre shows you.
        self.talks: list[Talk] = []

    def add_talk(self, talk: Talk) -> None:
        self.talks.append(talk)

    def calendar(self) -> str:
        """Return a string calendar of talks sorted by start time."""

        def get_hour(talk: Talk) -> int:
            return talk.hour

        sorted_talks = sorted(self.talks, key=get_hour)
        talks = "\n".join(str(talk) for talk in sorted_talks)
        return f"{self.year} PyCon at {self.location}\n{talks}"


pycon = PyCon("Salt Lake City", 2022)
pycon.add_talk(Talk("Securing Code with the Type System", 11))
pycon.add_talk(Talk("Cool Talk", 14))
pycon.add_talk(Talk("Cool Talk II", 15))
print(pycon.calendar())
print(f"The first talk is {pycon.talks[0]}")
