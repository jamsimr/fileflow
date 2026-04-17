from datetime import datetime

def write_log(message: str, log_file: str) -> None:
    """Append a single log message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")