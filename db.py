import sqlite3


def init_db():
    with sqlite3.connect("sqlite3.db") as conn:
         c = conn.cursor()
         c.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
         conn.commit()

init_db()


def get_students():
    with sqlite3.connect("sqlite3.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM student")

        # list of tuples
        return c.fetchall()
def insert_student(name, age):
    with sqlite3.connect("sqlite3.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO student (name, age) VALUES (?, ?)", (name, age))
        conn.commit()


def update_student(id, name=None, age=None):
    if not name and not age:
        return

    with sqlite3.connect("sqlite3.db") as conn:
        c = conn.cursor()
        if name and age:
            c.execute("UPDATE student SET age=?, name=? WHERE id=?", (age, name, id))
        elif name:
            c.execute("UPDATE student SET name=? WHERE id=?", (name, id))
        elif age:
            c.execute("UPDATE student SET age=? WHERE id=?", (age, id))
        conn.commit()


def delete_student(id):
    with sqlite3.connect("sqlite3.db") as conn:
        c = conn.cursor()
        c.execute("DELETE FROM student WHERE id=?", (id,))
        conn.commit()


def get_student(id):
    with sqlite3.connect("sqlite3.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM student WHERE id=?", (id,))
        return c.fetchone()
