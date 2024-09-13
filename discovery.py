import os
import numpy as np

def discover_files(directory, extensions=None):
    file_paths = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has the desired extension
            if extensions and not file.lower().endswith(extensions):
                continue
            # Construct the full file path
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    # Convert the list to a NumPy array
    file_paths_array = np.array(file_paths)
    return file_paths_array

if __name__ == "__main__":
    # Take input from the user for the directory path
    directory = input("Enter the directory path: ")

    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
    else:
        # Define the image file extensions to look for
        image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

        # Discover files and store them in a NumPy array
        all_files_array = discover_files(directory, image_extensions)

        # Save the array to a .npy file for communication with DatasetLoading.py
        np.save('file_paths.npy', all_files_array)

        # Print the number of images found
        print(f"Number of images found: {len(all_files_array)}")
        print("File paths saved to 'file_paths.npy'")
