import sqlite3

"""with sqlite3.connect('my_data_base.db') as conection:
    cursor = conection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    born_date TEXT
    )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
    )
    ''')
    cursor.execute("INSERT INTO authors (name, born_date) VALUES ('Davi Barros', '2001-12-10');")
    cursor.execute("INSERT INTO books (title, author_id) VALUES ('Python basico', 1);")
    cursor.execute("INSERT INTO books (title, author_id) VALUES ('Django basico', 1);")
    cursor.execute("INSERT INTO authors (name, born_date) VALUES ('Caio Sampaio', '2000-06-21');")
    cursor.execute("INSERT INTO books (title, author_id) VALUES ('Python full', 2);")
conection.close()"""

"""name = input("Digite seu nome: ")
with sqlite3.connect('my_data_base.db') as conection:
    cursor = conection.cursor()
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
"""
with sqlite3.connect(r'aulas-pythonando-main\python_full\m04_banco_dados\my_data_base.db') as conection:
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    for author in authors:
        print(author[1])
