from typing import Optional
import os
import boto3
from botocore.exceptions import ClientError
from pokemendel_core.utils.download_images import (
    download_pokemon_from_google_search,
    download_gym_from_google_search,
    download_pokemon_type_from_google_search
)

# Cloudflare R2 configuration
R2_ACCOUNT_ID = "c06bad2747e4a6177cecd8e31e326a3f"
R2_ENDPOINT_URL = f"https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com"
R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME", "pokemendel")  # Default bucket name, can be overridden via env var
R2_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY")

def _get_r2_client():
    """Get a boto3 client configured for Cloudflare R2."""
    if not R2_ACCESS_KEY_ID or not R2_SECRET_ACCESS_KEY:
        raise ValueError("R2_ACCESS_KEY_ID and R2_SECRET_ACCESS_KEY must be set in environment variables")
    
    return boto3.client(
        's3',
        endpoint_url=R2_ENDPOINT_URL,
        aws_access_key_id=R2_ACCESS_KEY_ID,
        aws_secret_access_key=R2_SECRET_ACCESS_KEY,
        region_name='auto'  # R2 uses 'auto' as the region
    )

s3_client = _get_r2_client()
buckets = s3_client.list_buckets()
print([b['Name'] for b in buckets['Buckets']])
