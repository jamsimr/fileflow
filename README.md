# FileFlow

A lightweight Python command-line tool for organising files from a shared input folder.

## Version 1.0 - 15 April 2026

### Minimum Viable Product

FileFlow can:
- read files from an input folder
- validate filenames against a naming standard
- move valid files to a processed folder
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
3. Check results in `data/processed/` and `data/quarantine/`
4. View logs in `data/logs/`

### Naming Standard

All files must follow: `category_YYYYMMDD_description.ext`

Categories: report, invoice, meeting, image
Extensions: .pdf, .csv, .txt, .jpg, .png

Example: `report_20260415_webex-performance.pdf`

### Project Structure

```
fileflow/
├── app/              # Main code
├── data/             # Folders for files
├── scripts/          # Helper scripts
└── README.md         # This file
```

    