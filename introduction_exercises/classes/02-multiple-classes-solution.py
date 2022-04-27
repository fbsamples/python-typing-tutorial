# Step 1: Annotate the constructor and methods of the `PyCon` class.
# Step 2: Identify the bug present in one or more of the three calls at the end.

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
        self.talks: list[Talk] = []

    def add_talk(self, talk: Talk) -> None:
        self.talks.append(talk)

    def calendar(self) -> str:
        """Return a string calendar of talks sorted by start time."""

        def get_start_hour(talk: Talk) -> int:
            return talk.start_hour

        sorted_talks = sorted(self.talks, key=get_start_hour)
        talks = "\n".join(str(talk) for talk in sorted_talks)
        return f"{self.year} PyCon at {self.location}\n{talks}"


pycon = PyCon("Salt Lake City", 2022)
pycon.add_talk(Talk("Securing Code with the Type System", 11))
pycon.add_talk("Python Typing Tutorial")
pycon.add_talk([Talk("Cool Talk", 14), Talk("Cool Talk II", 15)])
print(pycon.calendar())
