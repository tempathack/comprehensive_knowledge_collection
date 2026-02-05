"""
Script to update Plotly notebooks for Jupyter Book compatibility.

The issue: `fig.show()` doesn't embed properly in Jupyter Book static HTML.
The fix: Replace `fig.show()` with just `fig` at the end of cells.

Run this script from the root of your Jupyter Book project:
    python fix_plotly_notebooks.py

This will:
1. Find all .ipynb files (excluding _build directory)
2. Replace `fig.show()` at the end of code cells with just `fig`
3. Save the modified notebooks
"""

import json
import re
from pathlib import Path


def fix_notebook(notebook_path: Path) -> bool:
    """
    Fix Plotly fig.show() calls in a notebook.
    Returns True if changes were made.
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    modified = False
    
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') != 'code':
            continue
        
        source = cell.get('source', [])
        if isinstance(source, str):
            source = source.split('\n')
        
        # Check if this cell has fig.show() that should be replaced
        new_source = []
        cell_modified = False
        
        for i, line in enumerate(source):
            # Match fig.show() at the end of a line (possibly with comments)
            # Handles: fig.show(), fig.show() # comment, etc.
            if re.match(r'^\s*fig\.show\(\)\s*(#.*)?$', line):
                # Check if this is the last non-empty line
                remaining = [l for l in source[i+1:] if l.strip()]
                if not remaining:
                    # Replace fig.show() with fig
                    indent = len(line) - len(line.lstrip())
                    new_line = ' ' * indent + 'fig'
                    if '#' in line:
                        comment = line[line.index('#'):]
                        new_line += '  ' + comment
                    new_source.append(new_line)
                    cell_modified = True
                    continue
            new_source.append(line)
        
        if cell_modified:
            cell['source'] = new_source
            modified = True
    
    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"  Fixed: {notebook_path}")
    
    return modified


def main():
    root = Path('.')
    
    # Find all notebooks excluding _build
    notebooks = [
        p for p in root.rglob('*.ipynb')
        if '_build' not in str(p) and '.ipynb_checkpoints' not in str(p)
    ]
    
    print(f"Found {len(notebooks)} notebooks to check...")
    
    fixed_count = 0
    for nb_path in notebooks:
        try:
            if fix_notebook(nb_path):
                fixed_count += 1
        except Exception as e:
            print(f"  Error processing {nb_path}: {e}")
    
    print(f"\nDone! Fixed {fixed_count} notebooks.")
    print("\nNext steps:")
    print("1. Clear your Jupyter Book cache: jupyter-book clean . --all")
    print("2. Rebuild: jupyter-book build .")


if __name__ == '__main__':
    main()
