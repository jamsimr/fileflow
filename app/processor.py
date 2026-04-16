import os
import shutil

from app.logger import write_log
from app.validator import is_valid_filename

def process_files(input_folder: str, processed_folder: str, quarantine_folder: str, log_file: str) -> dict:
    """Scan the input folder, validate each filename, move valid files to processed, move invalid files to quarantine, write a simple log and return summary counts."""
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
            write_log(f"VALID: {filename} -> {destination}", log_file)
            counts["processed"] += 1
        else:
            destination = os.path.join(quarantine_folder, filename)
            shutil.move(file_path, destination)
            print(f"Quarantined: {filename}")
            write_log(f"INVALID: {filename} -> {destination}", log_file)
            counts["quarantined"] += 1

    return counts