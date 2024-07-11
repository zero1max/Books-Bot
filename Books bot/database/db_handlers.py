import sqlite3
from dataclasses import dataclass

@dataclass
class Database:
    connect: sqlite3.Connection = None
    cursor: sqlite3.Cursor = None

    def __post_init__(self):
        self.connect = sqlite3.connect('bookdata.db')
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS books(
                            id INTEGER PRIMARY KEY,
                            book_id TEXT NOT NULL,
                            book_name TEXT NOT NULL
                )""")
        self.connect.commit()

    def add_books(self, book_id, book_name):
        self.cursor.execute("INSERT INTO books (book_id, book_name) VALUES (?, ?)", (book_id, book_name))
        self.connect.commit()

    def select_books(self):
        self.cursor.execute("SELECT * FROM books") 
        return self.cursor.fetchall()

    def select_book(self, book_name):
        self.cursor.execute("SELECT * FROM books WHERE  book_name = ?", (book_name,))
        return self.cursor.fetchone()
    
    def delete_one(self, value):
        self.cursor.execute(f"DELETE FROM books WHERE book_name=?",(value,))
        self.connect.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM books")
        self.connect.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()