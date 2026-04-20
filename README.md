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
4. Make the CLI executable:
   ```bash
   chmod +x fileflow
   ```
5. (Optional but recommended) Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

### Usage

1. Place files in the `data/input/` folder
2. 
2. Run FileFlow using the CLI command:
   ```bash
   chmod +x fileflow
   ./fileflow
   ```
3. Use optional CLI flags for additional behaviour:
   ```bash
   ./fileflow --verbose
   ./fileflow --dry-run
   ./fileflow --config config/config.json
   ```
4. Check results in category subfolders under `data/processed/` (reports/, invoices/, meetings/, images/) and `data/quarantine/`
5. View logs in `data/logs/`

### Command-line options

FileFlow supports the following CLI options:

- `--config PATH`: Path to the config file (default: `config/config.json`)
- `--verbose`: Print detailed step-by-step information during processing
- `--dry-run`: Preview actions without moving or modifying any files

### CLI Wrapper

FileFlow can be run using the `fileflow` command via the included CLI wrapper script:

```bash
./fileflow
```

This script:
- ensures the correct working directory is used
- activates the virtual environment if present
- passes all CLI arguments through to the application

This provides a clean, user-friendly interface compared to running Python modules directly.

### Scripts

FileFlow includes several bash scripts in the `scripts/` folder:

Before running any scripts run `chmod +x scripts/*.sh`

- **`run_fileflow.sh`**: Main script to run FileFlow. Processes files from input folder and organizes valid files by category.
- **`run_fileflow_docker.sh`**: Run FileFlow in a Docker environment.
- **`seed_test_data.sh`**: Generates sample files with valid and invalid names for testing.
- **`reset_data.sh`**: Clears all files from data folders to start fresh.

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

### Archiving and Duplicate Handling

FileFlow includes an archive system to manage repeated processing of valid files and prevent data loss.

#### Archive Behaviour

When a valid file is processed, FileFlow checks whether a file with the same name already exists in the corresponding `processed/` subfolder.

- If no existing file is found:
  - The file is moved directly to `processed/`
- If a file with the same name already exists:
  - The existing file is moved to the `archive/` folder
  - The new file replaces it in `processed/`

This ensures that the `processed/` folder always contains the latest version of each file, while older versions are preserved in `archive/`.

#### Archive Structure

Archived files are stored in category-specific subfolders, mirroring the structure of `processed/`:

- `archive/reports/`
- `archive/invoices/`
- `archive/meetings/`
- `archive/images/`

#### Duplicate Handling in Archive

If multiple versions of the same file are archived, FileFlow ensures that no files are overwritten.

- The first archived file keeps its original name
- Subsequent archived versions are renamed with an incrementing suffix:
  - `report_20260415_sales-summary.pdf`
  - `report_20260415_sales-summary_1.pdf`
  - `report_20260415_sales-summary_2.pdf`

This behaviour is implemented using a helper function that checks for existing filenames and generates a unique destination.

#### Summary Metrics

FileFlow tracks the following archive-related metrics during execution:

- `archived`: Number of processed files that were moved to archive
- `archive_duplicates`: Number of times an archived file required renaming due to a naming collision

These metrics are included in both console output and generated reports, providing visibility into file versioning behaviour.

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

    