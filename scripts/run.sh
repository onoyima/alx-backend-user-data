#!/bin/bash
# Run the main Python script and check for pycodestyle compliance

echo "Running the main script..."
python3 ../0x00-personal_data/main.py

echo "Checking code style with pycodestyle..."
pycodestyle ../0x00-personal_data/
