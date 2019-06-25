from pathlib import Path
import json


# ***Working with JSON Files***

movies = [
    {"id": 1, "title": "Venom", "year": 2018},
    {"id": 2, "title": "Deadpool", "year": 2016},
]

data = json.dumps(movies)
path = Path('movies.json')
path.write_text(data)

data = path.read_text()
movies = json.loads(data)
print(movies[0])
