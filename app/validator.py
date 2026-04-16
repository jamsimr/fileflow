import re

# Matches:
# category_YYYYMMDD_description.ext
# Example:
# report_20240101_sales-summary.csv
FILENAME_PATTERN = re.compile(
    r'^(?:report|invoice|meeting|image)'
    r'_(?:\d{4}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01]))'
    r'_[A-Za-z0-9_-]+'
    r'\.(?:pdf|csv|txt|jpg|png)$'
)

def is_valid_filename(filename: str) -> bool:
    """Check if the filename matches the expected pattern."""
    return bool(FILENAME_PATTERN.match(filename))