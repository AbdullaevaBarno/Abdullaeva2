import sqlite3
from datetime import datetime
db = sqlite3.connect("flower_shop.db")
cursor = db.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    surname TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
# cursor.execute("""
# ALTER TABLE users ADD COLUMN surname TEXT;
# """)
db.commit()


async def add_user(telegram_id, name,surname, phone):
    cursor.execute("""INSERT INTO users (telegram_id, name, surname, phone)
                   VALUES (?, ?, ?, ?)
                   """, (telegram_id, name, surname, phone))
    db.commit()
async def add_review(telegram_id, review_text):
        cursor.execute("""
            INSERT INTO reviews (telegram_id, review_text) 
            VALUES (?, ?)
        """, (telegram_id, review_text))
        db.commit()
        
    
def show_users():
    db = sqlite3.connect("flower_shop.db")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()
def show_reviews():
    db = sqlite3.connect("flower_shop.db")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM reviews')
    return cursor.fetchall()
def close_db():
    db.close()