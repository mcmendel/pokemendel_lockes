"""Cloudflare R2 storage integration module.

This module provides functions for interacting with Cloudflare R2 storage,
including uploading, downloading, and checking for file existence.
"""

from typing import Optional
import os
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Cloudflare R2 configuration
R2_ACCOUNT_ID = "c06bad2747e4a6177cecd8e31e326a3f"
R2_ENDPOINT_URL = f"https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com"


def get_r2_client():
    """Get a boto3 client configured for Cloudflare R2.
    
    Returns:
        A configured boto3 S3 client for R2
        
    Raises:
        ValueError: If R2_ACCESS_KEY_ID or R2_SECRET_ACCESS_KEY are not set
    """
    # Re-read environment variables at runtime to ensure they're current
    access_key_id = os.getenv("R2_ACCESS_KEY_ID")
    secret_access_key = os.getenv("R2_SECRET_ACCESS_KEY")
    bucket_name = os.getenv("R2_BUCKET_NAME", "pokemendel")
    
    # Strip ALL whitespace (leading, trailing, and any internal issues)
    # This is critical - even a single space will cause SignatureDoesNotMatch
    if access_key_id:
        access_key_id = access_key_id.strip()
        # Also remove any newlines or carriage returns that might have been copied
        access_key_id = access_key_id.replace('\n', '').replace('\r', '').replace('\t', '')
    if secret_access_key:
        secret_access_key = secret_access_key.strip()
        # Also remove any newlines or carriage returns that might have been copied
        secret_access_key = secret_access_key.replace('\n', '').replace('\r', '').replace('\t', '')
    if bucket_name:
        bucket_name = bucket_name.strip()
    
    if not access_key_id or not secret_access_key:
        raise ValueError("R2_ACCESS_KEY_ID and R2_SECRET_ACCESS_KEY must be set in environment variables")
    
    # Debug: Check if credentials are set (without printing the actual values)
    access_key_set = bool(access_key_id)
    secret_key_set = bool(secret_access_key)
    print(f"DEBUG: R2 credentials check - Access Key ID set: {access_key_set}, Secret Key set: {secret_key_set}")
    print(f"DEBUG: R2 config - Bucket: '{bucket_name}', Endpoint: {R2_ENDPOINT_URL}")
    print(f"DEBUG: Access Key ID starts with: {access_key_id[:8]}..., length: {len(access_key_id)}")
    print(f"DEBUG: Secret Key length: {len(secret_access_key)}")
    
    # Check for whitespace issues
    if access_key_id and (access_key_id != access_key_id.strip() or '\n' in access_key_id or '\r' in access_key_id):
        print(f"WARNING: Access Key ID had whitespace issues - cleaned")
    if secret_access_key and (secret_access_key != secret_access_key.strip() or '\n' in secret_access_key or '\r' in secret_access_key):
        print(f"WARNING: Secret Key had whitespace issues - cleaned")
    
    # Verify credentials match expected format
    expected_access_key_start = "b0690286"
    if access_key_id and not access_key_id.startswith(expected_access_key_start):
        print(f"WARNING: Access Key ID doesn't start with expected value! Got: {access_key_id[:8]}...")
    
    # Use the exact same configuration as the test script that worked
    # Important: Don't use any additional parameters that might affect signature calculation
    config = Config(
        signature_version='s3v4',
        s3={
            'addressing_style': 'path'
        },
        # Disable any automatic retries or additional processing
        retries={'max_attempts': 1}
    )
    
    # Create client with explicit parameters - match test script exactly
    client = boto3.client(
        's3',
        endpoint_url=R2_ENDPOINT_URL,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name='auto',
        config=config
    )
    
    print(f"DEBUG: Created S3 client successfully")
    return client


def get_bucket_name() -> str:
    """Get the R2 bucket name from environment variables.
    
    Returns:
        The bucket name, defaulting to 'pokemendel' if not set
    """
    bucket_name = os.getenv("R2_BUCKET_NAME", "pokemendel")
    if bucket_name:
        bucket_name = bucket_name.strip()
    return bucket_name


def check_file_exists(s3_key: str) -> bool:
    """Check if a file exists in R2.
    
    Args:
        s3_key: The S3 key (path) to check
        
    Returns:
        True if file exists, False otherwise
    """
    try:
        s3_client = get_r2_client()
        bucket_name = get_bucket_name()
        s3_client.head_object(Bucket=bucket_name, Key=s3_key)
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            return False
        elif error_code == '403':
            # 403 means forbidden - likely token doesn't have Object Read permission
            # Treat as not found to allow fallback to download
            print(f"WARNING: Access forbidden (403) when checking R2 for '{s3_key}'. "
                  f"This may indicate the API token needs 'Object Read' or 'Admin Read' permissions. "
                  f"Falling back to local download.")
            return False
        else:
            print(f"Error checking R2: {error_code} - {e.response['Error']['Message']}")
            raise


def upload_file(local_file_path: str, s3_key: str) -> str:
    """Upload a local file to R2.
    
    Args:
        local_file_path: Path to the local file to upload
        s3_key: The S3 key (path) where the file should be stored
        
    Returns:
        The S3 key path
        
    Raises:
        Exception: If the upload fails
    """
    bucket_name = get_bucket_name()
    
    # Determine content type based on file extension
    content_type = 'image/jpeg'
    if local_file_path.lower().endswith('.png'):
        content_type = 'image/png'
    elif local_file_path.lower().endswith('.jpg'):
        content_type = 'image/jpeg'
    
    # Debug: Print what we're about to upload
    print(f"DEBUG: Uploading to R2 - bucket='{bucket_name}', key='{s3_key}', endpoint='{R2_ENDPOINT_URL}'")
    print(f"DEBUG: Local file exists: {os.path.exists(local_file_path)}, size: {os.path.getsize(local_file_path) if os.path.exists(local_file_path) else 'N/A'} bytes")
    
    # Create a fresh client for each upload to avoid any state issues
    s3_client = get_r2_client()
    
    try:
        # Try using upload_file first (like the test script that worked)
        # This method handles file reading and upload in one call
        print(f"DEBUG: Attempting upload_file method (like test script)")
        s3_client.upload_file(
            local_file_path,
            bucket_name,
            s3_key,
            ExtraArgs={'ContentType': content_type}
        )
        print(f"DEBUG: upload_file completed successfully")
        
        # Verify the upload by checking if the object exists
        try:
            verify_response = s3_client.head_object(Bucket=bucket_name, Key=s3_key)
            print(f"Successfully uploaded and verified in R2: bucket={bucket_name}, key={s3_key}, size={verify_response['ContentLength']} bytes")
        except ClientError as verify_e:
            error_code = verify_e.response.get('Error', {}).get('Code', 'Unknown')
            if error_code == '403':
                print(f"WARNING: Upload succeeded but verification returned 403 (permissions issue)")
            else:
                print(f"WARNING: Upload appeared to succeed but verification failed: {verify_e}")
            # Still return the key since upload_file succeeded
            print(f"Returning S3 key anyway: {s3_key}")
        
        return s3_key
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        print(f"ERROR uploading to R2:")
        print(f"  Bucket: {bucket_name}")
        print(f"  Key: {s3_key}")
        print(f"  Endpoint: {R2_ENDPOINT_URL}")
        print(f"  Error Code: {error_code}")
        print(f"  Error Message: {error_message}")
        # Re-raise with more context
        raise Exception(f"Failed to upload {local_file_path} to {bucket_name}/{s3_key}: {error_code} - {error_message}") from e
    except Exception as e:
        print(f"ERROR uploading to R2 (non-ClientError): {type(e).__name__}: {e}")
        raise


def download_file(s3_key: str) -> Optional[bytes]:
    """Download a file from R2.
    
    Args:
        s3_key: The S3 key (path) of the file to download
        
    Returns:
        File contents as bytes, or None if not found
        
    Raises:
        ClientError: If there's an error downloading (other than file not found)
    """
    try:
        s3_client = get_r2_client()
        bucket_name = get_bucket_name()
        response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        return response['Body'].read()
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return None
        raise


def is_s3_path(path: str) -> bool:
    """Check if a path is an S3 key path.
    
    Args:
        path: The path to check
        
    Returns:
        True if it's an S3 path, False otherwise
    """
    return path.startswith("pokemendel/resources/")


def extract_base_name_and_extension(file_path: str) -> tuple[str, str]:
    """Extract base name and extension from a file path, handling multiple extensions.
    
    For files like 'meganium.png.jpeg', this will return ('meganium', '.jpeg')
    For files like 'charizard.png', this will return ('charizard', '.png')
    
    Args:
        file_path: Full path to the file
        
    Returns:
        Tuple of (base_name, extension) where base_name has no extensions
    """
    base_filename = os.path.basename(file_path)
    
    # Split on all extensions - find the last one
    parts = base_filename.rsplit('.', 1)
    if len(parts) == 2:
        base_name = parts[0]
        ext = '.' + parts[1]
        # Remove any additional extensions from base_name
        # Handle cases like 'meganium.png' -> base should be 'meganium'
        if '.' in base_name:
            # If there's still a dot, take the first part as the true base name
            base_name = base_name.split('.')[0]
    else:
        base_name = base_filename
        ext = '.jpeg'  # Default extension
    
    return base_name, ext

