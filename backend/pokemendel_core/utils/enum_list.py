"""
Generic base class for enum-like classes with list functionality.
"""
from typing import List, Type, TypeVar, Any

T = TypeVar('T', bound='EnumList')

class EnumListMeta(type):
    """Metaclass for EnumList to make class attributes immutable."""
    
    def __setattr__(cls, name: str, value: Any) -> None:
        """Prevent modification of class attributes after definition."""
        raise AttributeError(f"Cannot modify {cls.__name__} constants")

class EnumList(metaclass=EnumListMeta):
    """Base class for enum-like classes that need listing functionality."""
    
    @classmethod
    def list_all(cls: Type[T]) -> List[str]:
        """Returns a list of all string constants defined in the class.
        
        Returns:
            List[str]: A list containing all string constant values.
        """
        return [
            value for name, value in vars(cls).items()
            if not name.startswith('_') and isinstance(value, str)
        ] 