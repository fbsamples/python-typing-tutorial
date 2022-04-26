# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# TODO: Try type-annotate the following function, so the entire file would type
# check. Please avoid using union type.


def close_all(*things):
    for t in things:
        t.close()


import tarfile, threading


class Resource:
    def __init__(self, lock: threading.Lock) -> None:
        self.lock = lock

    def acquire(self) -> None:
        self.lock.acquire()

    def close(self) -> None:
        self.lock.release()


def test(resource: Resource, input_filename: str, output_filename: str) -> None:
    try:
        resource.acquire()
        in_file = tarfile.open(input_filename)
        out_file = open(output_filename, "w")
    finally:
        close_all(resource, in_file, out_file)
