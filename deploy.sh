#!/bin/bash

# Build and Deploy Script for PyBricks
# This script builds the project (strips type annotations) and deploys to the robot

set -e  # Exit on any error

echo "Building project for PyBricks..."
.venv/Scripts/python.exe utils/build.py

echo "Deploying to PyBricks robot 'Fums'..."
python -m pybricksdev run ble -n Fums build/main.py

echo "Build and deployment complete!"