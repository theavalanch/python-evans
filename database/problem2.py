# import sqlite3
# conn = sqlite3.connect('school.db')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY,
#                name TEXT,
#                subject TEXT,
#                grade TEXT
#                ) """)
# initial_data = ("""id =1, name = "john Doe", subject = "Math", grade = "A""")
# initial_data = ("""id =2, name = "jane smith", subject = "science", grade = "B""")
# initial_data = ("""id =3, name = "Alex johnson", subject = "English", grade = "C""")
  
# cursor.execute("""INSERT INTO students(id,name,subject,grade) VALUES(?,?,?,)":,initial_data""")
# cursor.execute("""INSERT INTO students(id,name,subject,grade) VALUES(?,?,?,)":,initial_data""")
# cursor.execute("""INSERT INTO students(id,name,subject,grade) VALUES(?,?,?,)":,initial_data""")

# cursor.execute("INSERT INTO students(name,subject, grade) VALUES(?,?,?,)",("Maria Garcia", "History","A"))
# cursor.execute("""UPDATE students SET grade =?, WHERE name =?, AND subject =?', ("A", "Jane smith", "Science")""")
# cursor.execute("""DELETE FROM students WHERE name =?, AND subject =?', ("Alex johnson", "Math")""")
# cursor.execute("SELECT * FROM students")
# all_records = cursor.fetchall()
# for record in all_records:
#     print(record)               
               


# # problem 2




















































