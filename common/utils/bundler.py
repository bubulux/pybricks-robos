#!/usr/bin/env python3
"""
Bundle Python files for PyBricks deployment by inlining all local imports.
PyBricks only supports single-file deployments, so this script resolves all
local imports and creates standalone files.
"""

import re
from pathlib import Path
from typing import Set


def resolve_imports(file_path: Path, processed: Set[str] = None) -> str:
    """
    Recursively resolve all local imports and return bundled code.
    
    Args:
        file_path: Path to the Python file to bundle
        processed: Set of already processed files to avoid circular imports
    
    Returns:
        Bundled Python code with all local imports inlined
    """
    if processed is None:
        processed = set()
    
    # Normalize path and check if already processed
    file_path = file_path.resolve()
    if str(file_path) in processed:
        return ""
    
    processed.add(str(file_path))
    
    if not file_path.exists():
        return f"# ERROR: Could not find {file_path}\n"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    bundled_lines = []
    imported_code = []
    
    for line in lines:
        # Match: from common.module.submodule import Something
        # or: from .module import Something (relative imports)
        match_from = re.match(r'^from\s+(common\.[.\w]+|\.[\w.]*)\s+import\s+(.+)$', line.strip())
        
        if match_from:
            module_path = match_from.group(1)
            # imports = match_from.group(2)
            
            # Convert module path to file path
            if module_path.startswith('common.'):
                # Absolute import from common
                parts = module_path.split('.')
                import_file = Path('common') / '/'.join(parts[1:])
            elif module_path.startswith('.'):
                # Relative import
                parent_dir = file_path.parent
                rel_parts = module_path.lstrip('.').split('.')
                
                # Count leading dots for parent directory navigation
                dots = len(module_path) - len(module_path.lstrip('.'))
                for _ in range(dots - 1):
                    parent_dir = parent_dir.parent
                
                if rel_parts and rel_parts[0]:
                    import_file = parent_dir / '/'.join(rel_parts)
                else:
                    import_file = parent_dir
            else:
                # Not a local import, keep it
                bundled_lines.append(line)
                continue
            
            # Try with .py extension or as __init__.py in a directory
            candidates = [
                import_file.with_suffix('.py'),
                import_file / '__init__.py',
                import_file / 'index.py',
            ]
            
            resolved_file = None
            for candidate in candidates:
                if candidate.exists():
                    resolved_file = candidate
                    break
            
            if resolved_file:
                # Recursively resolve imports in the imported file
                try:
                    rel_path = resolved_file.relative_to(Path.cwd())
                except ValueError:
                    rel_path = resolved_file
                imported_code.append(f"\n# === Bundled from {rel_path} ===")
                imported_code.append(resolve_imports(resolved_file, processed))
            else:
                # Could not resolve, keep original import
                bundled_lines.append(line)
        
        elif re.match(r'^import\s+(common\.[.\w]+)$', line.strip()):
            # Simple import statement (less common in this codebase)
            bundled_lines.append(line)
        
        else:
            # Not an import line, keep it
            bundled_lines.append(line)
    
    # Return imported code first, then the file's own code
    result = '\n'.join(imported_code)
    if result:
        result += '\n\n'
    result += '\n'.join(bundled_lines)
    
    return result


def bundle_file(source_file: Path, output_file: Path):
    """Bundle a Python file with all its local imports inlined."""
    bundled_code = resolve_imports(source_file)
    
    # Write to output file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(bundled_code)


if __name__ == "__main__":
    from argparse import ArgumentParser
    
    parser = ArgumentParser(description="Bundle Python files for PyBricks")
    parser.add_argument("source", help="Source Python file")
    parser.add_argument("output", help="Output bundled Python file")
    args = parser.parse_args()
    
    bundle_file(Path(args.source), Path(args.output))
    print(f"Bundled {args.source} -> {args.output}")
