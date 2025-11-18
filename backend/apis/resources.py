from typing import Optional
import os
from pokemendel_core.utils.download_images import (
    download_pokemon_from_google_search,
    download_gym_from_google_search,
    download_pokemon_type_from_google_search
)
from core.r2 import (
    check_file_exists,
    upload_file,
    download_file,
    is_s3_path,
    extract_base_name_and_extension
)

def get_pokemon_info(pokemon_name: str) -> Optional[str]:
    """
    Get Pokemon image path from R2, downloading and uploading if necessary.
    
    Args:
        pokemon_name: The name of the Pokemon to look up
        
    Returns:
        S3 key path to the Pokemon image in R2 or None if not found
    """
    # Check if image exists in R2 with common extensions
    pokemon_name_lower = pokemon_name.lower()
    for ext in ['.jpeg', '.jpg', '.png']:
        s3_key = f"pokemendel/resources/pokemons/{pokemon_name_lower}{ext}"
        if check_file_exists(s3_key):
            return s3_key
    
    # Image doesn't exist in R2, download it locally
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    local_path = download_pokemon_from_google_search(pokemon_name, resources_path)
    
    if local_path is None:
        return None
    
    # Extract base name and extension from the downloaded file
    # This handles files with multiple extensions like 'meganium.png.jpeg'
    base_name, ext = extract_base_name_and_extension(local_path)
    
    # Use the clean base name (without any extensions) to construct S3 key
    s3_key = f"pokemendel/resources/pokemons/{base_name.lower()}{ext}"
    
    # Upload to R2
    try:
        uploaded_s3_key = upload_file(local_path, s3_key)
        print(f"DEBUG: Upload successful, returning S3 key: {uploaded_s3_key}")
        return uploaded_s3_key
    except Exception as e:
        print(f"ERROR uploading Pokemon image to R2: {type(e).__name__}: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        # Fallback to local path if upload fails
        print(f"DEBUG: Falling back to local path: {local_path}")
        return local_path

def get_gym_leader_info(game_name: str, gym_name: str) -> Optional[str]:
    """
    Get gym leader image path from R2, downloading and uploading if necessary.
    
    Args:
        game_name: The name of the game (e.g., 'red', 'blue', 'gold', etc.)
        gym_name: The name of the gym leader
        
    Returns:
        S3 key path to the gym leader image in R2 or None if not found
    """
    # Check if image exists in R2 with common extensions
    game_name_lower = game_name.lower()
    gym_name_lower = gym_name.lower()
    for ext in ['.jpeg', '.jpg', '.png']:
        s3_key = f"pokemendel/resources/gyms/{game_name_lower}/{gym_name_lower}{ext}"
        if check_file_exists(s3_key):
            return s3_key
    
    # Image doesn't exist in R2, download it locally
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    local_path = download_gym_from_google_search(
        gym_name=gym_name,
        badge_name=gym_name,  # Use gym name as badge name
        location=game_name,   # Use game name as location
        resources_path=resources_path
    )
    
    if local_path is None:
        return None
    
    # Extract base name and extension from the downloaded file
    # This handles files with multiple extensions
    base_name, ext = extract_base_name_and_extension(local_path)
    
    # Use the clean base name (without any extensions) to construct S3 key
    s3_key = f"pokemendel/resources/gyms/{game_name_lower}/{base_name.lower()}{ext}"
    
    # Upload to R2
    try:
        return upload_file(local_path, s3_key)
    except Exception as e:
        print(f"Error uploading gym leader image to R2: {e}")
        # Fallback to local path if upload fails
        return local_path

def get_type_info(type_name: str) -> Optional[str]:
    """
    Get Pokemon type image path from R2, downloading and uploading if necessary.
    
    Args:
        type_name: The name of the Pokemon type (e.g., 'fire', 'water', etc.)
        
    Returns:
        S3 key path to the type image in R2 or None if not found
    """
    # Check if image exists in R2 with common extensions
    type_name_lower = type_name.lower()
    for ext in ['.jpeg', '.jpg', '.png']:
        s3_key = f"pokemendel/resources/types/{type_name_lower}{ext}"
        if check_file_exists(s3_key):
            return s3_key
    
    # Image doesn't exist in R2, download it locally
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
    local_path = download_pokemon_type_from_google_search(type_name, resources_path)
    
    if local_path is None:
        return None
    
    # Extract base name and extension from the downloaded file
    # This handles files with multiple extensions
    base_name, ext = extract_base_name_and_extension(local_path)
    
    # Use the clean base name (without any extensions) to construct S3 key
    s3_key = f"pokemendel/resources/types/{base_name.lower()}{ext}"
    
    # Upload to R2
    try:
        return upload_file(local_path, s3_key)
    except Exception as e:
        print(f"Error uploading type image to R2: {e}")
        # Fallback to local path if upload fails
        return local_path
