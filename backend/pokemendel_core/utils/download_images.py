"""
Utility for downloading Pokemon-related images from Google Image Search.
"""
import logging
import os
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import argparse
from PIL import Image
from io import BytesIO

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
DEFAULT_IMG_TYPE = "jpeg"
GOOGLE_BASE_URL = "https://www.google.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

class ImageDownloadError(Exception):
    """Custom exception for image download failures."""
    pass

class GoogleImageSearch:
    """Class for searching and downloading images from Google Image Search."""
    
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries

    def _validate_image(self, img_data: bytes) -> bool:
        """Validate that the downloaded data is a valid image.
        
        Args:
            img_data: Raw image data
            
        Returns:
            bool: True if valid image, False otherwise
        """
        try:
            Image.open(BytesIO(img_data))
            return True
        except Exception:
            return False

    def fetch_links_by_search(self, search_query: str, destination_path: str) -> Optional[str]:
        """Search for and download the first valid image result.
        
        Args:
            search_query: The search term to look for
            destination_path: Where to save the downloaded image
            
        Returns:
            Optional[str]: Path to saved image if successful, None otherwise
            
        Raises:
            ImageDownloadError: If no valid images could be downloaded
        """
        search_url = f"{GOOGLE_BASE_URL}/search?q={search_query}&tbm=isch"
        
        for attempt in range(self.max_retries):
            try:
                response = requests.get(search_url, headers=HEADERS, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                img_tags = soup.find_all("img")
                
                for img_tag in img_tags:
                    if img_tag.get('alt') == 'Google':
                        continue

                    img_url = img_tag.get("src")
                    if not img_url or img_url.startswith('data:image'):
                        continue

                    if img_url.startswith('/'):
                        img_url = urljoin(GOOGLE_BASE_URL, img_url)

                    logger.info(f"Attempting to download image from: {img_url}")
                    
                    try:
                        img_response = requests.get(img_url, timeout=10)
                        img_response.raise_for_status()
                        img_data = img_response.content
                        
                        if not self._validate_image(img_data):
                            logger.warning(f"Invalid image data from {img_url}")
                            continue
                            
                        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                        with open(destination_path, 'wb') as f:
                            f.write(img_data)
                            
                        logger.info(f"Successfully saved image to {destination_path}")
                        return destination_path
                        
                    except requests.RequestException as e:
                        logger.warning(f"Failed to download image from {img_url}: {e}")
                        continue
                        
                logger.warning(f"No valid images found on attempt {attempt + 1}")
                
            except requests.RequestException as e:
                logger.error(f"Search request failed on attempt {attempt + 1}: {e}")
                if attempt == self.max_retries - 1:
                    raise ImageDownloadError(f"Failed to complete search after {self.max_retries} attempts")
                    
        raise ImageDownloadError("No valid images found")


def download_from_google_search(
    search: str,
    local_dir: str,
    resources_path: str,
    output_filename: Optional[str] = None
) -> Optional[str]:
    """Download an image from Google Search results.
    
    Args:
        search: Search query
        local_dir: Subdirectory to save in
        resources_path: Base path for resources
        output_filename: Optional custom filename
        
    Returns:
        Optional[str]: Path to saved image if successful, None otherwise
    """
    try:
        output_filename = output_filename or search
        local_path = os.path.join(resources_path, local_dir, output_filename)
        
        if os.path.exists(local_path):
            logger.info(f"Image {output_filename} already exists in {local_dir}")
            return local_path

        google_searcher = GoogleImageSearch()
        return google_searcher.fetch_links_by_search(search, local_path)
        
    except Exception as e:
        logger.error(f"Error downloading image: {e}")
        return None


def download_pokemon_from_google_search(pokemon_name: str, resources_path: str) -> Optional[str]:
    """Download a Pokemon image.
    
    Args:
        pokemon_name: Name of the Pokemon
        resources_path: Base path for resources
        
    Returns:
        Optional[str]: Path to saved image if successful, None otherwise
    """
    search = f"pokemondb {pokemon_name}"
    logger.info(f"Downloading Pokemon: {pokemon_name}")
    return download_from_google_search(
        search=search,
        local_dir="pokemons",
        output_filename=f"{pokemon_name}.{DEFAULT_IMG_TYPE}",
        resources_path=resources_path,
    )


def download_gym_from_google_search(
    gym_name: str,
    badge_name: str,
    location: str,
    resources_path: str
) -> Optional[str]:
    """Download a gym badge image.
    
    Args:
        gym_name: Name of the gym
        badge_name: Name of the badge
        location: Location of the gym
        resources_path: Base path for resources
        
    Returns:
        Optional[str]: Path to saved image if successful, None otherwise
    """
    search_location = location.replace("_", " ")
    search = f"gym badge {badge_name} {search_location}"
    logger.info(f"Downloading gym badge: {badge_name} ({location})")
    return download_from_google_search(
        search=search,
        local_dir="gyms",
        output_filename=f"{gym_name}.{DEFAULT_IMG_TYPE}",
        resources_path=resources_path,
    )


def download_pokemon_type_from_google_search(pokemon_type: str, resources_path: str) -> Optional[str]:
    """Download a Pokemon type symbol image.
    
    Args:
        pokemon_type: The type to download
        resources_path: Base path for resources
        
    Returns:
        Optional[str]: Path to saved image if successful, None otherwise
    """
    search = f"pokemon type symbol {pokemon_type}"
    logger.info(f"Downloading type symbol: {pokemon_type}")
    return download_from_google_search(
        search=search,
        local_dir="types",
        output_filename=f"{pokemon_type}.{DEFAULT_IMG_TYPE}",
        resources_path=resources_path,
    )


def main():
    """Main entry point for command line usage."""
    parser = argparse.ArgumentParser(description='Pokemon Image Downloader')
    parser.add_argument('--pokemon-name', type=str, help='Pokemon to download')
    parser.add_argument('--gym-output-name', type=str, help='Output name for gym image')
    parser.add_argument('--pokemon-type', type=str, help='Pokemon type to download')
    parser.add_argument('--gym-badge', type=str, help='Badge name')
    parser.add_argument('--gym-location', type=str, help='Gym location')
    parser.add_argument('--resources-path', type=str, required=True, help='Path to store resources')
    
    args = parser.parse_args()
    
    if args.pokemon_name:
        download_pokemon_from_google_search(args.pokemon_name, args.resources_path)

    if args.gym_output_name and args.gym_badge and args.gym_location:
        download_gym_from_google_search(
            args.gym_output_name,
            args.gym_badge,
            args.gym_location,
            args.resources_path
        )

    if args.pokemon_type:
        download_pokemon_type_from_google_search(args.pokemon_type, args.resources_path)


if __name__ == "__main__":
    main()
