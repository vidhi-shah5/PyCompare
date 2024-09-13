from PIL import Image
import hashing  # Importing the new hashing module
import logging

# Configure logging
logging.basicConfig(filename='proxy_processing.log', level=logging.ERROR)

# Initialize an empty list to store proxies
proxy_array = []

def process_image(image, file_path):
    """
    Process a single image by creating one proxy and rotating it at 90, 180, and 270 degrees for hashing.

    Input: PIL image object, file path
    Output: Proxy images added to the proxy_array and hash_array
    """
    global proxy_array

    try:
        print(f"Processing image: {file_path}")

        # Create one proxy (e.g., by resizing or converting to grayscale)
        proxy_image = image.convert('L')  # Example: convert to grayscale

        # Add the proxy image to the proxy_array
        proxy_array.append(proxy_image)
        print("Created proxy image.")

        # Rotate the proxy image at different angles and generate hashes
        rotations = [0, 90, 180, 270]
        for angle in rotations:
            rotated_image = proxy_image.rotate(angle)
            hashing.hash_proxy_image(rotated_image, file_path, angle)

    except Exception as e:
        logging.error(f"Error processing image {file_path}: {e}")
        print(f"Error processing image {file_path}: {e}")
