def write_log(message: str, log_file: str) -> None:
    """Append a single log message to the log file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(message + "\n")