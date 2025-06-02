"""Custom exceptions for the API."""

class RunCreationError(Exception):
    """Base exception for run creation errors."""
    status_code = 500
    message = "An error occurred during run creation"

class RunAlreadyExistsError(RunCreationError):
    """Raised when attempting to create a run that already exists."""
    status_code = 409
    message = "Run already exists"

class InvalidLockeTypeError(RunCreationError):
    """Raised when an invalid locke type is provided."""
    status_code = 400
    message = "Invalid locke type"

    def __init__(self, locke_type: str, available_types: list[str]):
        self.message = f"Invalid locke type: {locke_type}. Available types: {available_types}"
        super().__init__(self.message) 