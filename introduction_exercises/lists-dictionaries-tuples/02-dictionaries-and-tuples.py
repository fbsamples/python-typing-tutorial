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

    # Step 1: Annotate this constructor.
    def __init__(self, nrows, ncolumns):
        # Step 2: Annotate this attribute explicitly, since it is not being
        # passed in to the constructor.
        self.seating = {
            row: ["__" for column in range(ncolumns)] for row in range(nrows)
        }

    # Step 3: Annotate this method.
    # (If you get stuck, put a red sticky on your laptop.)
    def add_attendees(self, attendees):
        for (row, column, attendee) in attendees:
            first_name, last_name = attendee.split(" ")
            self.seating[row - 1][attendee] = first_name[0] + last_name[0]

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self.seating.values())

# Step 4: Identify a bug in the `add_attendees` method. Convince yourself that
# the Pyre error is legitimate. Did you catch that when you read the code?
