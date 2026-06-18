import hashlib
import os


def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file.

    SHA-256 is used because it is cryptographically secure and
    widely used in file integrity monitoring and digital forensics.
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except (IOError, OSError) as e:
        print(f"  [ERROR] Could not read {file_path}: {e}")
        return None


def scan_folder(folder_path):
    """Scan a folder and return a dictionary of relative paths to SHA-256 hashes.

    Returns:
        { "relative/path.txt": "abcdef123456..." }
    """
    file_hashes = {}
    if not os.path.isdir(folder_path):
        print(f"  [ERROR] Folder not found: {folder_path}")
        return file_hashes

    for root, dirs, files in os.walk(folder_path):
        for filename in sorted(files):
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, folder_path)
            file_hash = calculate_file_hash(full_path)
            if file_hash:
                file_hashes[relative_path] = file_hash

    return file_hashes
