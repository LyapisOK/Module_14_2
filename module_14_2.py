import sqlite3
import random
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
def filling_db():
    cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
    for i in range(1, 11):
        cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                        (f'User_{i}', f'student_{i}@Urban_U.ru', str(random.randint(20, 70)), "1000"))
def bd():
    for i in range(1,11,2):
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

    for i in range(1,11,3):
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

    cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
    users = cursor.fetchall()
    print(f"Записи в БД:")
    for user in users:
        print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

    cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
    cursor.execute("SELECT COUNT(*) FROM Users")
    all_users = cursor.fetchone()[0]
    print(f"-----\nВсего записей в БД: {all_users}")
    cursor.execute("SELECT AVG(balance) FROM Users")
    balance_avg = cursor.fetchone()[0]
    print(f"Средний баланс в БД {balance_avg}")
    connection.commit()
    connection.close()


#filling_db()
bd()