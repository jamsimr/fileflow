import csv
import os
from datetime import datetime

def print_summary(counts: dict) -> None:
    """Print a summary of the processing results."""
    print("Processing complete")
    print(f"Total files scanned: {counts['scanned']}")
    print(f"Total files processed: {counts['processed']}")
    print(f"Total files quarantined: {counts['quarantined']}")
    print(f"Total files archived: {counts['archived']}")

def write_csv_report(counts: dict, report_folder: str) -> None:
    """Write a CSV report of the processing results to the report folder."""
    os.makedirs(report_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(report_folder, f"report_{timestamp}.csv")

    with open(report_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Metric", "Count"])
        writer.writerow(["Scanned", counts["scanned"]])
        writer.writerow(["Processed", counts["processed"]])
        writer.writerow(["Quarantined", counts["quarantined"]])
        writer.writerow(["Archived", counts["archived"]])

    print(f"Report written to: {report_path}")