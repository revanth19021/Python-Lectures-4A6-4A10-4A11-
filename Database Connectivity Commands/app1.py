from flask import Flask,render_template
import sqlite3

# 1. import sqlite3
# 2. connect()
# 3. cursor()
# 4. execute()
# 5. commit()
# 6. close()


app=Flask(__name__)

connection=sqlite3.connect('student.db')

cursor=connection.cursor()

cursor.execute('''create table if not exists students(
    id integer primary key,
    name text,
    age integer,
    marks integer
)''')

print("Table created successfully")


# insert data into table


name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

cursor.execute(
    "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
    (name, age, marks)
)

connection.commit()
print("Student added successfully")


# cursor.execute('''insert into students (id,name, age, marks) values (1, 'Alice', 20, 85)''')
# cursor.execute('''insert into students (id,name, age, marks) values (2, 'Bob', 22, 90)''')
connection.commit() # save changes permanently

print("Data inserted successfully")


# read data from table
cursor.execute('''select * from students''')
rows=cursor.fetchall()

for i in rows:
    print(i)
# Insert data using USER INPUT

# Read specific data (WHERE condition)
cursor.execute("SELECT * FROM students WHERE marks > 80")
data = cursor.fetchall()

for row in data:
    print(row)

#Update data
cursor.execute("""
UPDATE students
SET marks = 95
WHERE name = 'Revanth'
""")

connection.commit()
print("Data updated")



# Delete data
cursor.execute("DELETE FROM students WHERE name = 'Sai'")
connection.commit()
print("Data deleted")


connection.close() # close the connection