# Development Commands

## Install dependencies
```bash
pip install -r requirements.txt
```

## Build for PyBricks (strips type annotations and typing imports)
```bash
# Use virtual environment Python
.venv/Scripts/python.exe utils/build.py
```

## Monitor PyBricks robot
```bash
# Monitor source code directly (for development)
.venv/Scripts/python.exe utils/monitor.py

# Build and monitor deployed version
./deployMonitored.sh
```

## Deploy to PyBricks robot
```bash
# Quick build and deploy script
./deploy.sh

# Build and monitor deployed version
./deployMonitored.sh

# Or build and deploy in one command
.venv/Scripts/python.exe utils/build.py && python -m pybricksdev run ble -n bubulux build/main.py

# Or deploy built version directly
python -m pybricksdev run ble -n bubulux build/main.py
```

## Development workflow
1. Write code with full type annotations in `src/` directory for better IDE support
2. Run build script: `.venv/Scripts/python.exe utils/build.py` 
3. This creates PyBricks-compatible version in `build/` directory (no typing imports or annotations)
4. Deploy with: `python -m pybricksdev run ble -n bubulux build/main.py`

## Utils
- `utils/build.py` - Build script that strips type annotations for PyBricks compatibility
- `utils/monitor.py` - Monitor script for robot output and debugging

## Quick Scripts
- `./deploy.sh` - Build and deploy to robot
- `./deployMonitored.sh` - Build and monitor deployed version

## Why this approach?
- PyBricks doesn't support the `typing` module (MicroPython limitation)
- You get full IDE support and static analysis during development
- Build process automatically strips incompatible code for deployment