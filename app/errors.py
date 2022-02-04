class BaseError(Exception):
    """Base error class."""
    def __init__(self, message: str) -> None:
        self.message = message


class ResourceNotFound(BaseError):
    """
    Indicate that the requested 
    resource doesn't exist.
    """
    pass