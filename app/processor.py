import os
import shutil

from app.logger import write_log
from app.validator import is_valid_filename

def get_unique_destination(destination: str) -> str:
    """If destination file already exists, append _1, _2, etc."""
    if not os.path.exists(destination):
        return destination
    
    base, ext = os.path.splitext(destination)
    counter = 1

    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1

    return f"{base}_{counter}{ext}"

def process_files(config: dict) -> dict:
    """Process files from input folder to processed or quarantine folders based on filename validation, and log the results."""
    input_folder = config["input_folder"]
    processed_folder = config["processed_folder"]
    quarantine_folder = config["quarantine_folder"]
    log_file = config["log_file"]
    filename_pattern = config["filename_pattern"]
    category_folders = config["category_folders"]

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)
    os.makedirs(quarantine_folder, exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    counts = {
        "scanned": 0,
        "processed": 0,
        "quarantined": 0,
        "archived": 0
    }

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip anything that is not a file
        if not os.path.isfile(file_path):
            continue

        counts["scanned"] += 1

        if is_valid_filename(filename):
            category = filename.split("_")[0]
            category_subfolder = category_folders[category]
            final_processed_folder = os.path.join(processed_folder, category_subfolder)
            os.makedirs(final_processed_folder, exist_ok=True)

            destination = os.path.join(final_processed_folder, filename)
            destination = get_unique_destination(destination)

            shutil.move(file_path, destination)
            print(f"Processed: {filename}")
            write_log(f"VALID: {filename} -> {destination}", log_file)
            counts["processed"] += 1
        else:
            destination = os.path.join(quarantine_folder, filename)
            destination = get_unique_destination(destination)

            shutil.move(file_path, destination)
            print(f"Quarantined: {filename}")
            write_log(f"INVALID: {filename} -> {destination}", log_file)
            counts["quarantined"] += 1

    return counts