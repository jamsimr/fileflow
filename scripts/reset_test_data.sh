#!/bin/bash

echo "Resetting test data..."

# Clear output folders
find data/processed -type f -delete
find data/quarantine -type f -delete
find data/logs -type f -delete

# Clear input
find data/input -type f -delete

echo "Done."