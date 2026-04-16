#!/bin/bash

echo "Resetting test data..."

# Clear output folders
find data/processed -type f ! -name ".gitkeep" -delete
find data/processed/images -type f ! -name ".gitkeep" -delete
find data/processed/invoices -type f ! -name ".gitkeep" -delete
find data/processed/meetings -type f ! -name ".gitkeep" -delete
find data/processed/reports -type f ! -name ".gitkeep" -delete
find data/quarantine -type f ! -name ".gitkeep" -delete
find data/reports -type f ! -name ".gitkeep" -delete
find data/logs -type f ! -name ".gitkeep" -delete

# Clear input
find data/input -type f ! -name ".gitkeep" -delete

echo "Done."