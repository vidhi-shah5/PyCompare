import os
import shutil
import hashing  # Importing the hashing module

def find_duplicates():
    """
    Find and return duplicate images based on their hashes.
    """
    seen_hashes = {}
    duplicates = []

    for hash_dict in hashing.hash_array:
        combined_hash = (hash_dict['SHA-256'], hash_dict['MD5'], hash_dict['SHA-1'], hash_dict['rotation'])
        if combined_hash in seen_hashes:
            duplicates.append(hash_dict)
        else:
            seen_hashes[combined_hash] = hash_dict

    return duplicates

def handle_duplicates(duplicates):
    """
    Provide options to handle duplicates: delete, move, or keep.
    """
    for duplicate in duplicates:
        print(f"Duplicate found: {duplicate['file_path']} with rotation {duplicate['rotation']}°")
        print("Options:")
        print("1. Delete one copy")
        print("2. Move one copy")
        print("3. Keep both copies")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            delete_duplicate(duplicate)
        elif choice == '2':
            move_duplicate(duplicate)
        elif choice == '3':
            print("Keeping both copies.")
        else:
            print("Invalid choice. Keeping both copies by default.")

def delete_duplicate(duplicate):
    """
    Delete one copy of the duplicate image.
    """
    file_path = duplicate['file_path']
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

def move_duplicate(duplicate):
    """
    Move one copy of the duplicate image to a specified directory.
    """
    file_path = duplicate['file_path']
    destination_dir = input("Enter the destination directory: ")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    try:
        shutil.move(file_path, destination_dir)
        print(f"Moved: {file_path} to {destination_dir}")
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

if __name__ == "__main__":
    # Find duplicates based on hashes
    duplicates = find_duplicates()

    # Handle duplicates based on user choice
    handle_duplicates(duplicates)
