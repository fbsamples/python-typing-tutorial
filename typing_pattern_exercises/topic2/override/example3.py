# pyre-ignore-all-errors

# TODO: Change `pyre-ignore-all-errors` to `pyre-strict` on line 1, so we get
# to see all type errors in this file.

# A (hypothetical) Python developer is having trouble with a typing-related
# issue. Here is what the code looks like:


class ConfigA:
    pass


class ConfigB:
    some_attribute: int = 1


class HelperBase:
    def __init__(self, config: ConfigA | ConfigB) -> None:
        self.config = config

    def common_fn(self) -> None:
        pass


class HelperA(HelperBase):
    def __init__(self, config: ConfigA) -> None:
        super().__init__(config)


class HelperB(HelperBase):
    def __init__(self, config: ConfigB) -> None:
        super().__init__(config)

    def some_fn(self) -> int:
        return self.config.some_attribute


# The developer is confused about why Pyre reports a type error on `HelperB.some_fn`.
# Question: Is the reported type error a false positive or not?
# Question: How would you suggest changing the code to avoid the type error?
# Question: Is it a good idea to have `HelperA` and `HelperB` share the same base class?
