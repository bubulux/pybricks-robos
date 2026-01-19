#!/usr/bin/env python3
"""
Build script to prepare source code for PyBricks deployment.
Bundles all imports into single files and strips type annotations.
"""

import shutil
import sys
from pathlib import Path

# Add common/utils to path so we can import bundler
sys.path.insert(0, str(Path(__file__).parent))
from bundler import resolve_imports

try:
    import strip_hints  # type: ignore
except ImportError:
    print("Error: strip-hints package not found. Install with: pip install strip-hints")
    exit(1)


def build_for_pybricks():
    """Build source files for PyBricks by bundling imports and stripping type annotations."""
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Build source files for PyBricks by bundling imports and stripping type annotations."
    )
    parser.add_argument("source_dir", nargs="?", default="src", help="Source directory")
    parser.add_argument("build_dir", nargs="?", default="build", help="Build directory")
    parser.add_argument("-s", "--silent", action="store_true", help="Suppress output")
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    build_dir = Path(args.build_dir)
    silent = args.silent

    def echo(msg):  # type: ignore
        if not silent:
            print(msg)  # type: ignore

    # Clean build directory
    if build_dir.exists():
        shutil.rmtree(build_dir)
    
    build_dir.mkdir(parents=True, exist_ok=True)

    # Find all main robot files (index.py files in src)
    robot_files = list(source_dir.rglob("index.py"))
    
    echo(f"Bundling {len(robot_files)} robot files...")

    for robot_file in robot_files:
        relative_path = robot_file.relative_to(source_dir)
        output_file = build_dir / relative_path
        
        echo(f"Bundling: {robot_file} -> {output_file}")
        
        # Bundle all imports into a single file
        bundled_code = resolve_imports(robot_file)
        
        # Strip type annotations from the bundled code
        try:
            # Write bundled code to temp file first
            temp_file = output_file.with_suffix('.temp.py')
            temp_file.parent.mkdir(parents=True, exist_ok=True)
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(bundled_code)
            
            stripped_code = strip_hints.strip_file_to_string(  # type: ignore
                str(temp_file), to_empty=True, strip_nl=False
            )
            
            # Clean up temp file
            temp_file.unlink()
            
            # Remove typing imports
            lines = stripped_code.split("\n")
            filtered_lines = []
            
            for line in lines:
                # Skip lines that import from typing module
                if line.strip().startswith("from typing ") or line.strip().startswith("import typing"):
                    continue
                filtered_lines.append(line)
            
            final_code = "\n".join(filtered_lines)
            
            # Write to output file
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(final_code)
                
        except Exception as e:
            echo(f"Warning: Failed to process {robot_file}: {e}")

    echo(f"Build complete! Files ready in '{build_dir}' directory")


if __name__ == "__main__":
    build_for_pybricks()
