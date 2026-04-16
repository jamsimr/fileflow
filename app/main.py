import os

from app.processor import process_files
from app.reporter import print_summary

def main() -> None:
    # Get project root directory."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_folder = os.path.join(project_root, "data", "input")
    processed_folder = os.path.join(project_root, "data", "processed")
    quarantine_folder = os.path.join(project_root, "data", "quarantine")
    log_file = os.path.join(project_root, "data", "processing.log")

    # Ensure input folder exists
    os.makedirs(input_folder, exist_ok=True)

    # Process files and get summary counts
    counts = process_files(input_folder=input_folder, processed_folder=processed_folder, quarantine_folder=quarantine_folder, log_file=log_file)
    print_summary(counts)

if __name__ == "__main__":
    main()