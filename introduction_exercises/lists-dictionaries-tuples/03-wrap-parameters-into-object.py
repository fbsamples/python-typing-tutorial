# In this exercise, you will see how one refactors with the aid of a type
# checker.

# Step 1: Add a new class `Attendee` to represent an attendee.

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
        # Step 2: Change the `list[str]` to `list[Attendee]`.
        # Run Pyre and let the errors guide you to the other changes you need
        # to make. Each time you change a caller, run Pyre to confirm that
        # you've fixed the error.
        self.seating: dict[int, list[str]] = {
            row: ["__" for column in range(ncolumns)] for row in range(nrows)
        }

    def add_attendees(self, attendees: list[tuple[int, int, str]]) -> None:
        for (row, column, attendee) in attendees:
            first_name, last_name = attendee.split(" ")
            self.seating[row - 1][column - 1] = first_name[0] + last_name[0]

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self.seating.values())

auditorium = Auditorium(3, 8)
auditorium.add_attendees([(2, 3, "Shannon Zhu"), (3, 8, "Jia Chen"),
                          (1, 6, "Alex Kassil"), (1, 1, "Pradeep Kumar")])
print(auditorium)
