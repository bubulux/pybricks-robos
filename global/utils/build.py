#!/usr/bin/env python3
"""
Build script to prepare source code for PyBricks deployment.
Strips type annotations and typing imports since PyBricks doesn't support them.
"""

import shutil
from pathlib import Path

try:
    import strip_hints  # type: ignore
except ImportError:
    print("Error: strip-hints package not found. Install with: pip install strip-hints")
    exit(1)


def build_for_pybricks():

    """Build source files for PyBricks by stripping type annotations."""
    import sys
    if len(sys.argv) > 1:
        source_dir = Path(sys.argv[1])
    else:
        source_dir = Path("src")
    if len(sys.argv) > 2:
        build_dir = Path(sys.argv[2])
    else:
        build_dir = Path("build")

    # Clean build directory
    if build_dir.exists():
        shutil.rmtree(build_dir)

    # Copy source files to build directory
    shutil.copytree(source_dir, build_dir)

    # Find all Python files in build directory
    python_files = list(build_dir.rglob("*.py"))

    print(f"Stripping type annotations from {len(python_files)} files...")

    for py_file in python_files:
        print(f"Processing: {py_file}")

        try:
            # Strip type annotations
            stripped_code = strip_hints.strip_file_to_string(  # type: ignore
                str(py_file), to_empty=True, strip_nl=False
            )

            # Only write if we got a string result
            if isinstance(stripped_code, str):
                # Also remove typing imports that are now unused
                lines = stripped_code.split("\n")
                filtered_lines = []

                for line in lines:
                    # Skip lines that import from typing module
                    if line.strip().startswith(
                        "from typing "
                    ) or line.strip().startswith("import typing"):
                        continue
                    filtered_lines.append(line)  # type: ignore

                # Join back and write
                final_code = "\n".join(filtered_lines)  # type: ignore
                with open(py_file, "w", encoding="utf-8") as f:
                    f.write(final_code)
            else:
                print(f"Warning: strip_hints returned unexpected type for {py_file}")

        except Exception as e:
            print(f"Warning: Failed to process {py_file}: {e}")

    print(f"Build complete! Files ready in '{build_dir}' directory")


if __name__ == "__main__":
    build_for_pybricks()
