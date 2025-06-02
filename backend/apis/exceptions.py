"""Custom exceptions for the API."""

class RunCreationError(Exception):
    """Base exception for run creation errors."""
    status_code = 500
    message = "An error occurred during run creation"

class RunAlreadyExistsError(RunCreationError):
    """Raised when attempting to create a run that already exists."""
    status_code = 409
    message = "Run already exists"

    def __str__(self) -> str:
        return "A run with this name already exists"

class InvalidLockeTypeError(RunCreationError):
    """Raised when an invalid locke type is provided."""
    status_code = 400
    message = "Invalid locke type"

    def __init__(self, locke_type: str, valid_types: list[str]):
        self.locke_type = locke_type
        self.valid_types = valid_types
        super().__init__()
    
    def __str__(self) -> str:
        return f"Invalid locke type: {self.locke_type}. Available types: {self.valid_types}"

class RunNotFoundError(RunCreationError):
    """Raised when a run is not found."""
    status_code = 404
    
    def __init__(self, run_name: str):
        self.run_name = run_name
        super().__init__()
    
    def __str__(self) -> str:
        return f"Run '{self.run_name}' not found"

class InvalidGameError(RunCreationError):
    """Raised when an invalid game name is provided."""
    status_code = 400
    
    def __init__(self, game_name: str):
        self.game_name = game_name
        super().__init__()
    
    def __str__(self) -> str:
        return f"Invalid game name: {self.game_name}" 