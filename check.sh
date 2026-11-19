#!/bin/bash

set -e

echo "================================"
echo "Course Listing Build Information"
echo "================================"

echo "Build Date:"
date

echo "Flask Version:"
python3 -c "from importlib.metadata import version; print(version('Flask'))"

echo "Build check completed successfully!"