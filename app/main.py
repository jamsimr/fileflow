import os

from app.config_loader import load_config
from app.processor import process_files
from app.reporter import print_summary, write_csv_report

def main() -> None:
    """Main entry point for FileFlow application. Sets up directory paths relative to project root, ensures input folder exists, processes files from input folder to processed or quarantine folders, and prints a summary of the processing results."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, "config","config.json")

    config = load_config(config_path)

    # Convert relative paths from config into project-root-based absolute paths
    for key in ["input_folder", "processed_folder", "quarantine_folder", "archive_folder", "report_folder", "log_file"]:
        config[key] = os.path.join(project_root, config[key])

    counts = process_files(config)
    
    print_summary(counts)
    write_csv_report(counts, config["report_folder"])

if __name__ == "__main__":
    main()