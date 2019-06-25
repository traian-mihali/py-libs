from pathlib import Path

# ***Working with Paths***

Path.home()
# Path.mkdir(Path() / 'src')
path = Path('package\__init__.py')
print(path.exists())
print(path.is_dir())
print(path.is_file())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# path.mkdir()
# path.rmdir()
path = path.with_name('file.txt')
print(path.absolute())
path = path.with_suffix('.txt')
print(path)
