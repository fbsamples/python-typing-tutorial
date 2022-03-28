from __future__ import annotations

class Auditorium:
    """
    >>> auditorium = Auditorium(3, 8)
    >>> auditorium.add_attendees([(1, 1, "Pradeep Kumar Srinivasan"), (2, 3, "Shannon Zhu"), (3, 8, "Jia Chen"), (1, 6, "Alex Kassil")])
    >>> print(auditorium)
    PS __ __ __ __ AK __ __
    __ __ SZ __ __ __ __ __
    __ __ __ __ __ __ __ JC
    """
    def __init__(self, rows: int, columns: int) -> None:
        self.seating: dict[int, dict[int, str]] = {row: {} for row in range(1, rows+1)}
        self.rows = rows
        self.columns = columns

    def add_attendees(self, attendees: list[tuple[int, int, str]]) -> None:
        for (row, column, attendee) in attendees:
            name_split = attendee.split(" ")
            self.seating[row][column] = name_split[0][0] + name_split[-1][0]

    def __str__(self) -> str:
        def format_row(seating_row: dict[int, str]) -> str:
            print(seating_row)
            return " ".join([seating_row.get(seat, "__") for seat in range(1, self.columns+1)])

        return "\n".join([format_row(self.seating[row]) for row in self.seating])
