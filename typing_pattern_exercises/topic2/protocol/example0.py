# pyre-strict

# Consider the following `read_and_process()` function, which reads data from
# somewhere, and process the data somehow.
def _process(message: bytes) -> None:
    ...


def read_and_process(input_channel):
    message = input_channel.readline()
    _process(message)


# Question: without additional context, what do think should be the type of the
# parameter `input_channel`?


# ----------------------------------------------------------------------------


# It seems like `input_channel` can be many things. For examle, we could pass
# an opened file to it:


def test_file(filename: str) -> None:
    # https://docs.python.org/3/library/functions.html#open
    with open(filename, "rb") as f:
        # The type of `f` here would be `io.BufferedReader`. You can confirm it
        # by adding a `reveal_type(f)`.
        read_and_process(f)


# We could also have the `input_channel` backed by a data stream from network:

import socket


class SocketInputChannel:
    def __init__(self, sock: socket.socket) -> None:
        self.sock = sock

    # NOTE: This is just a simple implementation for demonstration purpose
    # only. It is horribly efficient and therefore not recommended for any
    # practical purpose. In production code, you may want to either leverage
    # `sock.makefile()` or to use an in-memory buffer along with a larger
    # chunk size for `sock.recv()`
    def readline(self) -> bytes:
        line = b""
        while not line.endswith(b"\n"):
            # https://docs.python.org/3/library/socket.html#socket.socket.recv
            line += self.sock.recv(1)
        return line


def test_network(sock: socket.socket) -> None:
    read_and_process(SocketInputChannel(sock))


# And why not have an input channel backed by a in-memory bytes buffer, if for
# no other reason than to make it easier to do unit tests on the
# `read_and_process()` function?

import io


def test_bytes_buffer(content: bytes) -> None:
    # https://docs.python.org/3/library/io.html#io.BytesIO
    read_and_process(io.BytesIO(content))


# ----------------------------------------------------------------------------


# TODO: Given all the usages described in the previous section, try
# type-annotating the `read_and_process()` function appeared on top of this
# file, so all of its callers in this file type checks.

# Also think about the scenario where in the future, we may further extend our
# application and define more kinds of input channels (i.e. define more classes
# that offers a bytes-returning `readline()` method). Does the annotation you
# added before still work?
