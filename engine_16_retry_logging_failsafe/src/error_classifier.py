class BaseEngineError(Exception):
    """Base class for all engine-related errors"""


# RETRYABLE ERRORS
class NetworkError(BaseEngineError):
    pass


class TimeoutError(BaseEngineError):
    pass


class RateLimitError(BaseEngineError):
    pass


# NON-RETRYABLE ERRORS
class DataFormatError(BaseEngineError):
    pass


class AuthError(BaseEngineError):
    pass


class FatalError(BaseEngineError):
    pass


def is_retryable_error(error: Exception) -> bool:
    retryable_types = (
        NetworkError,
        TimeoutError,
        RateLimitError,
    )
    return isinstance(error, retryable_types)
