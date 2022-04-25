# pyre-strict

import pathlib

# Here is a simple function that takes a file path and return its content. Try
# add type annotations to this function.
def read_file(path):
    try:
        # https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text
        return path.read_text()
    except (FileNotFoundError, PermissionError) as error:
        return None


# Here is an alternative implementation that lets the exceptions escape. Try
# type annotating this one as well.
def read_file_alternative(path):
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text
    return path.read_text()


# Compare the two functions above. Which one is more convenient to use? Which
# one is safer to use?
def _process_content(data: str) -> None:
    ...


def test(path: pathlib.Path) -> None:
    file_content = read_file(path)
    if file_content is not None:  # what happens if we remove this line?
        _process_content(file_content)

    file_content2 = read_file_alternative(path)
    _process_content(file_content2)
