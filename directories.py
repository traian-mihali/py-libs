from pathlib import Path

# ***Working with Directories***

path = Path('package')
path.exists()
# path.mkdir()
# path.rmdir()
path.rename('package')
print([p for p in path.iterdir() if p.is_dir()])
# recursively
print([p for p in path.glob('**/*.py')])
print([p for p in path.rglob('*.py')])
