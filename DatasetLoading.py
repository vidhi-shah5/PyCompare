import numpy as np
from PIL import Image
import proxy  # Assuming proxy.py is in the same directory
import logging
import hashing

# Configure logging
logging.basicConfig(filename='image_processing.log', level=logging.ERROR)

def load_and_process_images(file_paths_array):
    for file_path in file_paths_array:
        try:
            # Load the image from the file path
            image = Image.open(file_path)
            # Pass the image and file path to the proxy method for processing
            proxy.process_image(image, file_path)
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")
            print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Load the NumPy array from the file saved by discovery.py
    file_paths_array = np.load('file_paths.npy')

    # Process the images by passing them to proxy.py
    load_and_process_images(file_paths_array)

    # Once all images are processed, print the total number of proxies created
    print(f"Total number of proxies created: {len(proxy.proxy_array)}")
    print(f"Total number of hashes created: {len(hashing.hash_array)}")
