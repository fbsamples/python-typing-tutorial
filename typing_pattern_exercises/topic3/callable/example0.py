# pyre-strict

# We have a query API like this, possibly taken from some network-oriented
# library. It takes the input of a query and two callbacks, and invoke the
# right callback depending on whether the query has succeeded or not.


def _do_query(inputs: str) -> str:
    ...


def query(inputs, on_success, on_failure):
    try:
        result = _do_query(inputs)
        on_success(result)
    except Exception as error:
        on_failure(error)


# The API can be used as follows:


def process_query_result(result: str) -> None:
    print(f"Query succeeded with result = {result}")


def log_error(error: Exception) -> None:
    print(f"Query failed with error = {error}")


def test(inputs: str) -> None:
    query(inputs, on_success=process_query_result, on_failure=log_error)


# Please fill in the type annotation of the `query` function, so the `test()`
# function could type check.
