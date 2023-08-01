import mysql.connector as mysql

db = mysql.connect(
    user='user1',
    password='AVNS_BIPHdghyp1-JLYypm-t',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='monstro'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students')
# print(cursor.fetchall())
#
# cursor.execute('SELECT * FROM students WHERE id = 1')
# print(cursor.fetchone())

# user_input = input('Enter ID: ')
# cursor.execute("SELECT * FROM students WHERE name = %s AND second_name = 'Antipin'", (user_input,))
# print(cursor.fetchall())

# cursor.execute("UPDATE students SET name='Ольга' WHERE id = 4")

# cursor.execute("DELETE FROM books WHERE id = 8")

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = [
    ('Vasia', 'Pupkin'),
    ('Ivan', 'Ivanov')
]
cursor.executemany(query, values)
db.commit()

db.close()
