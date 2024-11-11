import sqlite3


connection = sqlite3.connect("company.db")

# Create a cursor
cursor = connection.cursor()

# create a table
cursor.execute ("""CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name VARCHAR(5) NOT NULL,
                position TEXT,
                salary REAL
                );""")
name = 'jason'
position = 'human resource'
salary = 56000

#  Insert a row of data
cursor.execute("INSERT INTO employees(name, position,salary)VALUES('DAVID', 'secretary', 2300)")
cursor.execute("INSERT INTO employees(name, position,salary)VALUES('mason', 'general manager', 5300)")

# Insert a row of data using placeholders
# cursor.execute("INSERT INTO employees (name, position,salary) VALUES (?,?,?)",(name, position, salary))
# cursor.execute("INSERT INTO employees (name, position,salary) VALUES (?,?,?)",(name, position, salary))

# Select all data
cursor.execute("Select * FROM employees")
rows = (cursor.fetchall())
for row in rows:
    print(row)   
#  Update a row of data
cursor.execute("UPDATE employees SET salary = ? WHERE id = ?",(56000,4))
cursor.execute("UPDATE employees SET name = NULL WHERE id = 4")

