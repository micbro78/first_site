import sqlite3

print("Creating todo.db database")

conn = sqlite3.connect('todo.db')
conn.execute("CREATE TABLE todo (category char(50), item char(100), id INTEGER PRIMARY KEY)")
conn.execute("INSERT INTO todo (category, item) VALUES ('Shopping', 'eggs')")
conn.execute("INSERT INTO todo (category, item) VALUES ('Shopping', 'milk')")
conn.execute("INSERT INTO todo (category, item) VALUES ('Shopping', 'bread')")
conn.execute("INSERT INTO todo (category, item) VALUES ('Activities', 'Water the garden')")
conn.execute("INSERT INTO todo (category, item) VALUES ('Activities', 'Tidy my bedroom')")
conn.commit()

print("Database todo.db created")
