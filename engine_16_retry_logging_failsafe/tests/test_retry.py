import pytest
from retry_policy import retry_with_backoff
from error_classifier import NetworkError

counter = {"count": 0}

def unstable():
    counter["count"] += 1
    if counter["count"] < 2:
        raise NetworkError("fail")
    return "ok"

def test_retry_success():
    result = retry_with_backoff(
        unstable,
        exceptions=(NetworkError,),
        max_attempts=3,
        base_delay=0
    )
    assert result == "ok"
