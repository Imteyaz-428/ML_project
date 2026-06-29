from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10
    ),
    reraise=True
)
def retry_request(func, *args, **kwargs):

    return func(*args, **kwargs)