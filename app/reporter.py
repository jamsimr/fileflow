def print_summary(counts: dict) -> None:
    """Print a summary of the processing results."""
    print("Processing complete")
    print(f"Total files scanned: {counts['scanned']}")
    print(f"Total files processed: {counts['processed']}")
    print(f"Total files quarantined: {counts['quarantined']}")