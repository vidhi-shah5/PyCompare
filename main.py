import os
import numpy as np
from discovery import discover_files
from DatasetLoading import load_and_process_images
from compare_duplicates import find_duplicates, handle_duplicates

def main():
    # Input number of directories
    num_directories = int(input("Enter the number of directories to scan: "))
    directories = []

    # Input paths of all directories
    for i in range(num_directories):
        directory = input(f"Enter the path for directory {i + 1}: ")
        if os.path.isdir(directory):
            directories.append(directory)
        else:
            print(f"The directory '{directory}' does not exist. Please enter a valid directory.")
            return

    # Discover files in all directories
    all_files = []
    for directory in directories:
        files = discover_files(directory, extensions=('.jpg', '.jpeg', '.png', '.bmp', '.gif'))
        all_files.extend(files)

    # Convert the list to a NumPy array and save it
    all_files_array = np.array(all_files)
    np.save('file_paths.npy', all_files_array)

    # Process the images
    load_and_process_images(all_files_array)

    # Find and handle duplicates
    duplicates = find_duplicates()
    handle_duplicates(duplicates)

if __name__ == "__main__":
    main()
