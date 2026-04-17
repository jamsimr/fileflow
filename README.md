# FileFlow

A lightweight Python command-line tool for organising files from a shared input folder.

## Version 1.0 - 17 April 2026

### Minimum Viable Product

FileFlow can:
- read files from an input folder
- validate filenames against a naming standard
- move valid files to category-specific subfolders in processed/
- move invalid files to quarantine
- write a simple log of operations
- print a basic summary to the console

### Installation

1. Make sure you have Python 3.8+ installed
2. Clone or download this project
3. Navigate to the fileflow directory
4. Run: `python app/main.py`

### Usage

1. Place files in the `data/input/` folder
2. Run FileFlow using from the FileFlow directory: `./scripts/run_fileflow.sh`
3. Check results in category subfolders under `data/processed/` (reports/, invoices/, meetings/, images/) and `data/quarantine/`
4. View logs in `data/logs/`

### Scripts

FileFlow includes several helper scripts in the `scripts/` folder:

- **`run_fileflow.sh`**: Main script to run FileFlow. Processes files from input folder and organizes valid files by category.
- **`seed_test_data.sh`**: Generates sample files with valid and invalid names for testing.
- **`reset_test_data.sh`**: Clears all files from data folders to start fresh.

To use any script, navigate to the fileflow directory and run: `./scripts/script_name.sh`

### Naming Standard

All files must follow: `category_YYYYMMDD_description.ext`

Categories: report, invoice, meeting, image
Extensions: .pdf, .csv, .txt, .jpg, .png

Example: `report_20260415_webex-performance.pdf`

### File Organization

Valid files are automatically organized into category-specific subfolders under `data/processed/`:

- Files starting with `report_` → `data/processed/reports/`
- Files starting with `invoice_` → `data/processed/invoices/`
- Files starting with `meeting_` → `data/processed/meetings/`
- Files starting with `image_` → `data/processed/images/`

Invalid files are moved to `data/quarantine/` for review.

### Project Structure

```
fileflow/
├── app/                    # Main application code
├── data/                   # Runtime data folders
│   ├── input/             # Files to be processed
│   ├── processed/         # Valid files organized by category
│   │   ├── reports/       # Report files
│   │   ├── invoices/      # Invoice files
│   │   ├── meetings/      # Meeting files
│   │   └── images/        # Image files
│   ├── quarantine/        # Invalid files
│   ├── archive/           # Historical processed files
│   ├── report/            # Generated reports
│   └── logs/              # Application logs
├── scripts/               # Helper scripts
└── README.md              # This file
```

    