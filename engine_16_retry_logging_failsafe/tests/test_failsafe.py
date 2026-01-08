from failsafe_wrapper import failsafe_execute
from error_classifier import DataFormatError

def broken():
    raise DataFormatError("bad data")

def test_failsafe_does_not_crash():
    result = failsafe_execute(
        broken,
        job_context={"id": 1}
    )
    assert result is None
