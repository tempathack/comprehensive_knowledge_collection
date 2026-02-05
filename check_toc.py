import os
import yaml

# Read _toc.yml
with open('_toc.yml', 'r') as f:
    toc = yaml.safe_load(f)

# Extract all file entries from toc
def extract_files(obj, files=None):
    if files is None:
        files = set()
    if isinstance(obj, dict):
        if 'file' in obj:
            files.add(obj['file'])
        for v in obj.values():
            extract_files(v, files)
    elif isinstance(obj, list):
        for item in obj:
            extract_files(item, files)
    return files

toc_files = extract_files(toc)

# Get all .ipynb files (excluding _build and checkpoints)
actual_files = set()
for root, dirs, files in os.walk('.'):
    # Skip _build and checkpoint directories
    dirs[:] = [d for d in dirs if d not in ['_build', '.ipynb_checkpoints']]
    for f in files:
        if f.endswith('.ipynb'):
            rel_path = os.path.join(root, f)[2:]  # Remove ./
            rel_path = rel_path.replace('\\', '/').replace('.ipynb', '')
            actual_files.add(rel_path)

# Find missing from toc
missing_from_toc = actual_files - toc_files
# Find in toc but missing from filesystem  
missing_from_fs = toc_files - actual_files

print('=== NOTEBOOKS NOT IN _toc.yml ===')
for f in sorted(missing_from_toc):
    print(f'  {f}')

print(f'\nTotal missing from TOC: {len(missing_from_toc)}')

print('\n=== IN _toc.yml BUT FILE MISSING ===')
for f in sorted(missing_from_fs):
    print(f'  {f}')

print(f'\nTotal in TOC but missing: {len(missing_from_fs)}')
