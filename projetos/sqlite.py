import sqlite3

db = sqlite3.connect('crud.db')
cursor = db.cursor()

cursor.execute('''UPDATE users SET balance = 0 WHERE balance IS null ''')
cursor.execute('''SELECT * FROM users''')

users = cursor.fetchall()

for user in users:
    print(user)

db.commit()
db.close()

