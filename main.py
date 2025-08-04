import sqlite3
import os

def create_database():
    if os.path.exists("student.db"):
        os.remove("student.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)        
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)    
        ''')
def insert_sample_data(cursor):
    students = [
        (1,'Alice Johnson',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming','Dr. Anderson',3),
        (2, 'Web Development', 'Prof. Wilson',4),
        (3, 'Data Science', 'Dr. Taylor',3),
        (4, 'Mobile Apps', 'Prof. garcia',2)
    ]
    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)",courses)
    print("Sample data inserted successfully")

def basic_sql_operations(cursor):
    #1) SELECT ALL
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records :
        print(row[0],row[1],row[2],row[3])
        print(f"ID : {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    #2) SELECT Columns
    cursor.execute("SELECT name, age FROM Students")
    records = cursor.fetchall()
    print(records)

    #3) WHERE clause
    cursor.execute("SELECT * FROM Students WHERE age=20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #4) WHERE with String
    cursor.execute("SELECT * FROM Students WHERE city = 'New YOrk' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print("------------ORDER BY ------------")
    #5) ORDER BY
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #6) LIMIT
    print("-----------------------LIMIT by 3 -------------------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)

def sql_update_delete_insert_operations(conn,cursor):
    #1)INSERT
    cursor.execute("INSERT INTO Students VALUES (6,'Frank Miller',23,'frank@gmail.com','Miamai')")
    conn.commit()

    #2)UPDATE
    cursor.execute("UPDATE Students SET age=24 WHERE id=6")
    conn.commit()

    #3) DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_functions(cursor):
    # 1) COUNT
    print("----------------------COUNT-----------------------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    # result = cursor.fetchall()
    # print(result[0][0])
    result = cursor.fetchone()
    print(result[0])

    # 2) AVERAGE
    print("----------------------AVG-----------------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("----------------------MAx - MIN -----------------------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    print(result)
    max_age , min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("---------------------- GROUP BY -----------------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students Group By city")
    result = cursor.fetchall()
    print(result)

def main():
    conn,cursor = create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn,cursor)
        aggregate_functions(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()



if __name__ == "__main__":
    main()