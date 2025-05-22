#!/bin/bash

# Run tests
python -m pytest -v tests

# Clean up __pycache__ folders
find . -type d -name "__pycache__" -exec rm -r {} + 