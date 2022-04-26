# pyre-strict


def _receive_bytes_data() -> bytes:
    ...


# TODO: This is a function that's intended to receive data from the network.
# Try add type annotation to it using union type. This entire file should type
# check if you annotate it correctly.
def receive_data(encoding=None):
    bytes_data = _receive_bytes_data()
    if encoding is None:
        return bytes_data
    else:
        return bytes_data.decode(encoding)


# Code below are used to verify if your annotated the above function correctly.
def _process_bytes(data: bytes) -> None:
    ...


def _process_string(data: str) -> None:
    ...


def test() -> None:
    received_bytes = receive_data()
    if isinstance(received_bytes, bytes):
        _process_bytes(received_bytes)

    received_string = receive_data("utf-8")
    if isinstance(received_string, str):
        _process_string(received_string)


# Note the two isinstance() check in our test() function -- why do you think
# they exist? What happens if we removed them?
