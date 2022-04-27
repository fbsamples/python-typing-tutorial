# In this exercise, you will see how one refactors with the aid of a type
# checker.

# We have a new `Attendee` class below.
# Search for Step 1 below, where you will change the current `str`
# representation to an `Attendee`.

class Attendee:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        if self.name == "__":
            return self.name

        first_name, last_name = self.name.split(" ")
        return first_name[0] + last_name[0]

class Auditorium:
    """
    >>> auditorium = Auditorium(3, 8)
    >>> auditorium.add_attendees([(2, 3, "Shannon Zhu"), (3, 8, "Jia Chen"),
                                  (1, 6, "Alex Kassil"), (1, 1, "Pradeep Kumar")])
    >>> print(auditorium)
    PK __ __ __ __ AK __ __
    __ __ SZ __ __ __ __ __
    __ __ __ __ __ __ __ JC
    """

    def __init__(self, nrows: int, ncolumns: int) -> None:
        # Step 1: Change the `list[str]` to `list[Attendee]`.
        # Fix the Pyre errors that arise.
        self.seating: dict[int, list[Attendee]] = {
            row: [Attendee("__") for column in range(ncolumns)] for row in range(nrows)
        }

    def add_attendees(self, attendees: list[tuple[int, int, str]]) -> None:
        for (row, column, attendee_name) in attendees:
            self.seating[row - 1][column - 1] = Attendee(name=attendee_name)

    def __str__(self) -> str:
        return "\n".join(" ".join(str(attendee) for attendee in row) for row in self.seating.values())

auditorium = Auditorium(3, 8)
auditorium.add_attendees([(2, 3, "Shannon Zhu"), (3, 8, "Jia Chen"),
                          (1, 6, "Alex Kassil"), (1, 1, "Pradeep Kumar")])
print(auditorium)
