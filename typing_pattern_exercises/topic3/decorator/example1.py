# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# ParamSpec can be used for more than just preserving function signatures. It
# can also be used to perform certain signature transformations. Below is a
# decorator that turns arbitrary async function into a sync function that gets
# executed immediately:

import asyncio
import random


def to_sync(func):
    def wrapper(*args, **kwargs):
        # Require Python 3.7
        # https://docs.python.org/3/library/asyncio-task.html#asyncio.run
        return asyncio.run(func(*args, **kwargs))

    return wrapper


# Here are some examples on how this decorator can be used:


@to_sync
async def count(start: int, end: int) -> int:
    result = 0
    for i in range(start, end):
        print(f"Counting {i}")
        result += 1
        await asyncio.sleep(1)
    return result


async def sleeper(identifier: int, duration: float) -> None:
    print(f"Thread {identifier} goes to sleep for {duration} seconds...")
    await asyncio.sleep(duration)
    print(f"Thread {identifier} just wakes up.")


@to_sync
async def concurrent_sleepers(count: int) -> None:
    await asyncio.gather(*(sleeper(i, 2 * random.random()) for i in range(count)))


# Notice how we can now invoke those async functions in a sync context, after
# applying the decorator. You can also run this file with the Python
# interpreter to verify that it works.
def test() -> None:
    print(count(1, 3))
    print(count(4, 6))
    concurrent_sleepers(2)
    concurrent_sleepers(3)


test()

# TODO: Your exercise is to add type annotations to the `to_sync` decorator
# using `ParamSpec`. If you did it correctly, the entire file should type
# check.
# For your information, async functions can generally be typed with `Callable`s
# in the same way as normal functions, except that the return type needs to be
# wrapped in an `Awaitable`. For example:

from typing import Callable, Awaitable


async def f(x: int) -> str:
    ...


def take_async(g: Callable[[int], Awaitable[str]]) -> None:
    ...


take_async(f)  # This should type check
