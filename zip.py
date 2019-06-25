from pathlib import Path
from zipfile import ZipFile

# ***Working with Zip Files***

with ZipFile('files.zip', 'w') as zip:
    for path in Path('package').rglob('*.*'):
        zip.write(path)

with ZipFile('files.zip') as zip:
    print(zip.namelist())
    info = zip.getinfo('package/__init__.py')
    print(info.file_size)
    print(info.compress_size)
    zip.extractall('extract')
