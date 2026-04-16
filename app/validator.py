import re

def is_valid_filename(filename: str, filename_pattern: str) -> bool:
    """Return true if filename matches the configured pattern in config."""
    return bool(re.match(filename_pattern, filename))