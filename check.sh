#!/bin/bash

echo "================================"
echo "Course Listing Build Information"
echo "================================"

echo "Build Date:"
date

echo "Flask Version:"
python -c "import flask; print(flask.__version__)"

echo "Build check completed successfully!"