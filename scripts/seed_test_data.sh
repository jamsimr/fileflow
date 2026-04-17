#!/bin/bash

echo "Seeding FileFlow test data..."

# Valid files
touch data/input/report_20260415_sales-summary.pdf
touch data/input/invoice_20260410_supplier-abc.csv
touch data/input/meeting_20260411_team-sync.txt
touch data/input/image_20260409_warehouse-photo.jpg

# Invalid files
touch "data/input/sales report final.pdf"
touch data/input/invoice_april.csv
touch data/input/meetingnotes.txt
touch data/input/IMG1234.png

# Error-handling test file
touch data/input/trigger-error_20260417_test.txt

echo "Test files created."