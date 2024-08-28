import numpy as np
from PIL import Image
#import proxy  # Assuming proxy.py is in the same directory

def load_and_process_images(file_paths_array):
    for file_path in file_paths_array:
        try:
            # Load the image
            image = Image.open(file_path)
            # Pass the image to the proxy method for processing
            print("Done")
            #proxy.process_image(image)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Load the NumPy array from the file saved by Discovery.py
    file_paths_array = np.load('file_paths.npy')

    # Process the images
    load_and_process_images(file_paths_array)
