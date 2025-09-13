#!/bin/bash

# Build and Deploy Script for PyBricks
# This script builds the project (strips type annotations) and deploys to the robot

set -e  # Exit on any error

echo "Building project for PyBricks..."
.venv/Scripts/python.exe build.py

echo "Deploying to PyBricks robot 'bubulux'..."
python -m pybricksdev run ble -n bubulux build/main.py

echo "Build and deployment complete!"