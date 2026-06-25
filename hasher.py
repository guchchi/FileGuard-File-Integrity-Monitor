import hashlib
import os
from typing import Dict, Optional


def calculate_file_hash(file_path: str) -> Optional[str]:
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


def scan_folder(folder_path: str) -> Dict[str, str]:
    file_hashes: Dict[str, str] = {}
    if not os.path.isdir(folder_path):
        print(f"  [ERROR] Folder not found: {folder_path}")
        return file_hashes

    for root, _dirs, files in os.walk(folder_path):
        for filename in sorted(files):
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, folder_path)
            file_hash = calculate_file_hash(full_path)
            if file_hash:
                file_hashes[relative_path] = file_hash

    return file_hashes
