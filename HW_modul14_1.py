import sqlite3
connection = sqlite3.connect('not_telegram.db')
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
for i in range (1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = ?', (500, 0))
cursor.execute("SELECT id FROM Users") 
rows = cursor.fetchall()
for index in range(len(rows)): 
    if index % 3 == 0:  # Условие для определения третьей записи 
        cursor.execute("DELETE FROM Users WHERE id = ?", (rows[index][0],))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age < ? OR age > ?', (60, 60))
result = cursor.fetchall()
print(result)
connection.commit() #Сохраняет состояние бд перед закрытием
connection.close()