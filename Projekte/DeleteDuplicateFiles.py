import os
import hashlib

def hash_file(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """Find and delete duplicate files in a directory and its subdirectories."""
    files_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            file_name = os.path.basename(file_path)

            if (file_hash, file_name) in files_hashes:
                duplicates.append(file_path)
            else:
                files_hashes[(file_hash, file_name)] = file_path

    return duplicates

def delete_files(file_paths):
    """Delete files given their paths."""
    for file_path in file_paths:
        os.remove(file_path)
        print(f"Deleted: {file_path}")


if __name__ == "__main__":
    # Specify the directory to search for duplicate files
    directory_to_search = "C:\\temp\\test"

    # Find duplicate files
    duplicate_files = find_duplicate_files(directory_to_search)

    # Delete duplicate files
    delete_files(duplicate_files)

    print("Duplicate files deletion completed.")
