import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user3',
    passwd='AVNS_iuMmW_up9nn-E9szNOR',
    database='monstro'
)

cursor = db.cursor(dictionary=True)

#  insert student
query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Alex', 'Alexandrov')
cursor.execute(query, values)
cursor.execute('SELECT * FROM students')
print(cursor.fetchall())


#  insert books
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [
    ('Python lessons', '30'),
    ('Python programming', '30')
]
cursor.executemany(query, values)
cursor.execute('SELECT * FROM books')
print(cursor.fetchall())


#  insert group
query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values = ('Python group', '20-07-2023', '20-09-2024')
cursor.execute(query, values)
cursor.execute('SELECT * FROM `groups`')
print(cursor.fetchall())


#  update students with group_id
cursor.execute('UPDATE students SET group_id = 12 WHERE id = 30')
cursor.execute('SELECT * FROM students')
print(cursor.fetchall())


#  insert subjects
query = 'INSERT INTO subjects (title) VALUE (%s)'
values = [
    ('informatics',),
    ('history',)
]
cursor.executemany(query, values)
cursor.execute('SELECT * FROM subjects')
print(cursor.fetchall())


#  insert lessons
query = 'INSERT INTO lessons (title, subject_id) VALUE (%s, %s)'
values = [
    ('algorithms', '7'),
    ('functions', '7'),
    ('modern history', '8'),
    ('ancient wars', '8')
]
cursor.executemany(query, values)
cursor.execute('SELECT * FROM lessons')
print(cursor.fetchall())


#  insert marks
query = 'INSERT INTO marks (student_id, lesson_id, mark) VALUE (%s, %s, %s)'
values = [
    ('30', '12', '7'),
    ('30', '13', '8'),
    ('30', '14', '9'),
    ('30', '15', '10')
]
cursor.executemany(query, values)
cursor.execute('SELECT * FROM marks')
print(cursor.fetchall())


#  get all student's marks
cursor.execute('SELECT * FROM marks where student_id = 30')
print(cursor.fetchall())


#  get all student's books
cursor.execute('SELECT * FROM books where taken_by_student_id = 30')
print(cursor.fetchall())


#  get all student's marks with subjects
cursor.execute('SELECT marks.mark, subjects.title FROM marks '
               'JOIN lessons ON marks.lesson_id = lessons.id '
               'JOIN subjects ON lessons.subject_id = subjects.id where student_id = 30')
print(cursor.fetchall())


#  get all student's info
cursor.execute('SELECT students.name, students.second_name, `groups`.title, books.title, marks.mark, lessons.title, '
               'subjects.title FROM students '
               'JOIN `groups` ON students.group_id = `groups`.id '
               'JOIN books ON students.id = books.taken_by_student_id '
               'JOIN marks ON students.id = marks.student_id '
               'JOIN lessons ON marks.lesson_id = lessons.id '
               'JOIN subjects ON lessons.subject_id = subjects.id '
               'where student_id = 30')

db.commit()
db.close()
