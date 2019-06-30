import sqlite3


class Database:

    def __init__(self, db):    # This function is quite similar to constructor in other languages
        self.conn = sqlite3.connect(db)  # By using self conn is an attribute not the class rather than
                                         # just a normal variable
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT,"
                          " author TEXT,year INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):

            self.curr.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
            self.conn.commit()

    def view(self):
        self.curr.execute("SELECT * FROM books")
        rows = self.curr.fetchall()
        # self.conn.close()    because we can't operate on closed connection
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.curr.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.curr.fetchall()
        return rows

    def delete(self, id):
        self.curr.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.curr.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
