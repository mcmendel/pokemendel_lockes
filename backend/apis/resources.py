from typing import Optional
import os
from pokemendel_core.utils.download_images import (
    download_pokemon_from_google_search,
    download_gym_from_google_search,
    download_pokemon_type_from_google_search
)

def get_pokemon_info(pokemon_name: str) -> Optional[str]:
    """
    Get Pokemon image path using pokemendel_core's download utility.
    
    Args:
        pokemon_name: The name of the Pokemon to look up
        
    Returns:
        Path to the Pokemon image file or None if not found
    """
    # Use the resources directory in the backend folder
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    return download_pokemon_from_google_search(pokemon_name, resources_path)

def get_gym_leader_info(game_name: str, gym_name: str) -> Optional[str]:
    """
    Get gym leader image path using pokemendel_core's download utility.
    
    Args:
        game_name: The name of the game (e.g., 'red', 'blue', 'gold', etc.)
        gym_name: The name of the gym leader
        
    Returns:
        Path to the gym leader image file or None if not found
    """
    # Use the resources directory in the backend folder
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    return download_gym_from_google_search(
        gym_name=gym_name,
        badge_name=gym_name,  # Use gym name as badge name
        location=game_name,   # Use game name as location
        resources_path=resources_path
    )

def get_type_info(type_name: str) -> Optional[str]:
    """
    Get Pokemon type image path using pokemendel_core's download utility.
    
    Args:
        type_name: The name of the Pokemon type (e.g., 'fire', 'water', etc.)
        
    Returns:
        Path to the type image file or None if not found
    """
    # Use the resources directory in the backend folder
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    return download_pokemon_type_from_google_search(type_name, resources_path) 