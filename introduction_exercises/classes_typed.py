from __future__ import annotations

class Talk:
    """
    >>> str(Talk("Python Typing Tutorial", 10))
    '10:00 - Python Typing Tutorial'
    """
    def __init__(self, title: str, hour: int) -> None:
        self.title = title
        self.hour = hour

    def __str__(self) -> str:
        return f"{str(self.hour)}:00 - {self.title}"

class PyCon:
    """
    >>> pycon = PyCon("Salt Late City, Utah", 2022)
    >>> pycon.add_talks([Talk("Securing Python Applications with Pysa", 11), Talk("Python Typing Tutorial", 10)])
    >>> print(pycon.calendar())
    2022 PyCon at Salt Late City, Utah
    10:00 - Python Typing Tutorial
    11:00 - Securing Python Applications with Pysa
    """
    def __init__(self, location: str, year: int) -> None:
        self.location = location
        self.year = year
        self.talks: list[Talk] = []

    def add_talks(self, new_talks: list[Talk]) -> None:
        self.talks.extend(new_talks)

    def calendar(self) -> str:
        def get_hour(talk: Talk) -> int:
            return talk.hour
        sorted_talks = sorted(self.talks, key=get_hour)
        new_line = "\n"
        return f"{self}{new_line}{new_line.join([str(talk) for talk in sorted_talks])}"

    def __str__(self) -> str:
        return f"{self.year} PyCon at {self.location}"
