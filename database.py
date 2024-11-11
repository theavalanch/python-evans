import sqlite3

connection = sqlite3.connect("mtib.db")

# create a cursor
cursor = connection.cursor()

# create a table
cursor.execute("""CREATE TABLE  IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               email TEXT unique
               );""")
name = 'maya'
age = 20
email = 'maya12@gmail.com'

# Insert a row of data
# cursor.execute("INSERT INTO users (name, age, email) VALUES ('John', 30, 'john@gmail.com') ")
# cursor.execute("INSERT INTO users (name, age, email) VALUES ('Evans', 10, 'Evans@gmail.com') ")

# Insert a row of data using placeholders
# cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
# cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?)", (name,  email))

# Update a row of data 
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Toyin",3))
cursor.execute("UPDATE users SET age = NULL WHERE id = 1")

# Delete a row of data
cursor.execute("DELETE FROM users  WHERE email = 'john@gmail.com' ")

# Insert a column of data
# cursor.execute("ALTER TABLE users ADD COLUMN gender TEXT")

# Remove a column of data
# cursor.execute("ALTER TABLE users DROP COLUMN gender")

# Select all data
cursor.execute("SELECT * FROM users ORDER BY id DESC")
rows =(cursor.fetchall())
for row in rows:
    print(row)

# Save (commit) the changes
connection.commit()








# class work








































































































































