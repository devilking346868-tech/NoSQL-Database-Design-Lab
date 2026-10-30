import sqlite3 as sql
conn = sql.connect("StudentDB.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    RollNumber INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Semester INTEGER,
    CGPA REAL
)
""")
# Insert student records
students = [
    (101, "Rohit", "BCA", 5, 8.5),
    (102, "Amit", "BCA", 5, 8.2),
    (103, "Rahul", "MCA", 3, 8.7),
    (104, "Priya", "BCA", 5, 9.1),
    (105, "Neha", "MCA", 3, 8.9)
]

cursor.executemany("""
INSERT OR IGNORE INTO Students
(RollNumber, Name, Department, Semester, CGPA)
VALUES (?, ?, ?, ?, ?)
""", students)

conn.commit()

print("5 student records inserted successfully!")
conn.commit()

print("Students table created successfully!")
cursor.execute("SELECT * FROM Students")

for student in cursor.fetchall():
    print(student)

conn.close()