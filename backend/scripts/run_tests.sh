#!/bin/bash

# Run tests
{
   python3 -m pytest -v tests
} || {
    echo "Tests failed"
}

# Clean up __pycache__ folders
find . -type d -name "__pycache__" -exec rm -r {} + 
find . -type d -name ".pytest_cache" -exec rm -r {} + 