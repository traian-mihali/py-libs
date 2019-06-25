from pathlib import Path
import sqlite3
import json

# ***Working with SQLite Database***

# movies = json.loads(Path('movies.json').read_text())

# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))

#     connection.commit()

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # print(list(cursor))
    movies = cursor.fetchall()
    print(movies)
