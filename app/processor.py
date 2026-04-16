import os
import shutil
from fileflow.app.validator import is_valid_filename

def process_files(input_folder: str, processed_folder: str, quarantine_folder: str) -> dict:
    """Scan the input folder, validate each filename, move valid files to processed,move invalid files to quarantine, and return counts."""
    os.makedirs(processed_folder, exist_ok=True)
    os.makedirs(quarantine_folder, exist_ok=True)

    counts = {
        "scanned": 0,
        "processed": 0,
        "quarantined": 0,
    }

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip anything that is not a file
        if not os.path.isfile(file_path):
            continue

        counts["scanned"] += 1

        if is_valid_filename(filename):
            destination = os.path.join(processed_folder, filename)
            shutil.move(file_path, destination)
            print(f"Processed: {filename}")
            counts["processed"] += 1
        else:
            destination = os.path.join(quarantine_folder, filename)
            shutil.move(file_path, destination)
            print(f"Quarantined: {filename}")
            counts["quarantined"] += 1

    return counts