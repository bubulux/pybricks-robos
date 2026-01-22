#!/bin/bash

# Build and Monitor Script for PyBricks
# This script builds the project and then monitors the deployed version

set -e  # Exit on any error

echo "Building project for PyBricks..."
.venv/bin/python utils/build.py

echo "Starting monitoring of deployed version..."
.venv/bin/python utils/monitor.py 