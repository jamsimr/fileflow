#!/bin/bash

echo "Seeding FileFlow test data..."

# VALID FILES (all categories)
touch data/input/report_20260415_sales-summary.pdf
touch data/input/invoice_20260410_supplier-abc.csv
touch data/input/meeting_20260411_team-sync.txt
touch data/input/image_20260409_warehouse-photo.jpg

# INVALID FILES
touch "data/input/sales report final.pdf"
touch data/input/invoice_april.csv
touch data/input/meetingnotes.txt
touch data/input/IMG1234.png

echo "Test files created."