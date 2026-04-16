import os

from app.processor import process_files
from app.reporter import print_summary

def main() -> None:
    """Main entry point for FileFlow application. Sets up directory paths relative to project root, ensures input folder exists, processes files from input folder to processed or quarantine folders, and prints a summary of the processing results."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_folder = os.path.join(project_root, "data", "input")
    processed_folder = os.path.join(project_root, "data", "processed")
    quarantine_folder = os.path.join(project_root, "data", "quarantine")
    log_file = os.path.join(project_root, "data", "processing.log")

    os.makedirs(input_folder, exist_ok=True)

    counts = process_files(input_folder=input_folder, processed_folder=processed_folder, quarantine_folder=quarantine_folder, log_file=log_file)
    print_summary(counts)

if __name__ == "__main__":
    main()