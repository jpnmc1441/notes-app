#!/bin/bash
# Run from anywhere — always switches to the script's own directory first.
cd "$(dirname "$0")"

# Pick whichever Python 3 is available
if command -v python3 &>/dev/null; then
    PY=python3
elif command -v python &>/dev/null; then
    PY=python
else
    echo "ERROR: Python not found. Install Python 3 from https://www.python.org"
    read -p "Press Enter to close..."
    exit 1
fi

echo "Installing/updating dependencies..."
$PY -m pip install -r requirements.txt -q

echo "Starting Notes App — opening browser..."
$PY app.py
