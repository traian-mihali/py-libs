from pathlib import Path
from time import ctime
import shutil

# ***Working with Files***

source = Path('package/__init__.py')
target = Path() / '__init__.py'
source.exists()
source.rename('init.py')
source.unlink()

print(ctime(source.stat().st_ctime))
print(source.read_bytes())

with open('package/__init__.py', "r") as file:
    print(file)

source.write_text("print('__init__', __name__)")
target.write_text(source.read_text())
print(source.read_text())

shutil.copy(source, target)
