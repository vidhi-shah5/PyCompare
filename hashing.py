import hashlib
import io
from PIL import Image
import logging

# Configure logging
logging.basicConfig(filename='hashing_errors.log', level=logging.ERROR)

# Initialize an empty list to store hashes
hash_array = []

def hash_proxy_image(image, file_path, rotation):
    """
    Create three different hashes for the proxy image using SHA-256, MD5, and SHA-1.

    Input: PIL image object, file path, rotation angle
    Output: Hashes are appended to the hash_array
    """
    global hash_array

    try:
        # Convert image to bytes
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format='PNG')
        img_data = img_byte_array.getvalue()

        # Create hashes using SHA-256, MD5, and SHA-1
        sha256_hash = hashlib.sha256(img_data).hexdigest()
        md5_hash = hashlib.md5(img_data).hexdigest()
        sha1_hash = hashlib.sha1(img_data).hexdigest()

        # Append the hashes and file path to the hash_array
        hash_array.append({
            'SHA-256': sha256_hash,
            'MD5': md5_hash,
            'SHA-1': sha1_hash,
            'file_path': file_path,
            'rotation': rotation
        })

        print(f"Hashes created for {rotation}° rotation: SHA-256: {sha256_hash}, MD5: {md5_hash}, SHA-1: {sha1_hash}")

    except Exception as e:
        logging.error(f"Error hashing image: {e}")
        print(f"Error hashing image: {e}")
