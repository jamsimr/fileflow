import os
import shutil

from app.logger import write_log
from app.validator import is_valid_filename

def get_unique_destination(destination: str) -> tuple[str, bool]:
    """Return a unique destination"""
    if not os.path.exists(destination):
        return destination, False
    
    base, ext = os.path.splitext(destination)
    counter = 1

    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1

    return f"{base}_{counter}{ext}", True

def process_files(config: dict, verbose: bool = False, dry_run: bool = False) -> dict:
    """Process files from input folder to processed or quarantine folders based on filename validation, and log the results."""
    input_folder = config["input_folder"]
    processed_folder = config["processed_folder"]
    quarantine_folder = config["quarantine_folder"]
    log_file = config["log_file"]
    filename_pattern = config["filename_pattern"]
    category_folders = config["category_folders"]
    archive_folder = config["archive_folder"]

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)
    os.makedirs(quarantine_folder, exist_ok=True)
    os.makedirs(archive_folder, exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    counts = {
        "scanned": 0,
        "processed": 0,
        "quarantined": 0,
        "archived": 0,
        "archive_duplicates": 0,
    }

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

            # Skip placeholder and hidden files
        if filename.startswith("."):
            continue

        # Skip anything that is not a file
        if not os.path.isfile(file_path):
            continue

        counts["scanned"] += 1

        try:
            if is_valid_filename(filename, filename_pattern):
                category = filename.split("_")[0]
                category_subfolder = category_folders[category]
                final_processed_folder = os.path.join(processed_folder, category_subfolder)
                os.makedirs(final_processed_folder, exist_ok=True)

                destination = os.path.join(final_processed_folder, filename)

                was_archived, archive_duplicate_found = archive_existing_file(
                    destination=destination,
                    archive_folder=archive_folder,
                    category_subfolder=category_subfolder,
                    filename=filename,
                    log_file=log_file
                )
                
                if was_archived:
                    counts["archived"] += 1 
                
                if archive_duplicate_found:
                    counts["archive_duplicates"] += 1

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
        
        except Exception as error:
            print(f"Error processing {filename}: {error}")
            write_log(f"ERROR: {filename} -> {error}", log_file)

    return counts

def get_archive_destination(archive_folder: str, category_subfolder: str, filename: str) -> tuple[str, bool]:
    """
    Return a unique archive destination path and whether an archive duplicate was found.
    """
    archive_category_folder = os.path.join(archive_folder, category_subfolder)
    os.makedirs(archive_category_folder, exist_ok=True)

    destination = os.path.join(archive_category_folder, filename)

    if not os.path.exists(destination):
        return destination, False

    base, extension = os.path.splitext(destination)
    counter = 1

    while True:
        new_destination = f"{base}_{counter}{extension}"
        if not os.path.exists(new_destination):
            return new_destination, True
        counter += 1


def archive_existing_file(
    destination: str,
    archive_folder: str,
    category_subfolder: str,
    filename: str,
    log_file: str
) -> tuple[bool, bool]:
    """
    If a processed file already exists, move it to archive.

    Returns:
        (was_archived, archive_duplicate_found)
    """
    if not os.path.exists(destination):
        return False, False

    archive_destination, archive_duplicate_found = get_archive_destination(
        archive_folder=archive_folder,
        category_subfolder=category_subfolder,
        filename=filename
    )

    shutil.move(destination, archive_destination)
    write_log(f"ARCHIVED: {destination} -> {archive_destination}", log_file)

    return True, archive_duplicate_found