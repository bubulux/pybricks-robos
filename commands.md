# Development Commands

## Install dependencies
```bash
pip install -r requirements.txt
```

## Build for PyBricks (strips type annotations and typing imports)
```bash
# Use virtual environment Python
.venv/Scripts/python.exe build.py
```

## Deploy to PyBricks robot
```bash
# Quick build and deploy script
./deploy.sh

# Or build and deploy in one command
.venv/Scripts/python.exe build.py && python -m pybricksdev run ble -n bubulux build/main.py

# Or deploy built version directly
python -m pybricksdev run ble -n bubulux build/main.py
```

## Development workflow
1. Write code with full type annotations in `src/` directory for better IDE support
2. Run build script: `.venv/Scripts/python.exe build.py` 
3. This creates PyBricks-compatible version in `build/` directory (no typing imports or annotations)
4. Deploy with: `python -m pybricksdev run ble -n bubulux build/main.py`

## Why this approach?
- PyBricks doesn't support the `typing` module (MicroPython limitation)
- You get full IDE support and static analysis during development
- Build process automatically strips incompatible code for deployment