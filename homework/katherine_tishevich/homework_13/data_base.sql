INSERT INTO students (id, name, second_name, group_id)  VALUES (2433, 'Kate', 'Tishevich', 3);
INSERT INTO books(id, title, taken_by_student_id) VALUES (15, 'The Her', 2433);
INSERT INTO `groups` (id, title, start_date, end_date) VALUES (15, 'Kotiki', '15-01-1999', '15-02-2023');
INSERT INTO subjects (id, title) VALUES (20,'History');
INSERT INTO subjects (id, title) VALUES (21,'Math');
INSERT INTO subjects (id, title) VALUES (22,'OOP');
INSERT INTO lessons (id, title, subject_id) VALUES (20,'History',20);
INSERT INTO lessons (id, title, subject_id) VALUES (21,'Math',22);
INSERT INTO lessons (id, title, subject_id) VALUES (22,'OOP',22);
INSERT INTO lessons (id, title, subject_id) VALUES (23,'History of Belarus',20);
INSERT INTO lessons (id, title, subject_id) VALUES (24,'Math 9-11',22);
INSERT INTO lessons (id, title, subject_id) VALUES (25,'OOP concept',22);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (20,2433,20,9);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (21,2433,21,8);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (22,2433,22,9);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (23,2433,20,7);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (24,2433,21,10);
INSERT INTO marks (id, student_id, lesson_id, mark) VALUES (25,2433,22,9);
select mark from marks where student_id = 2433;
select title from books where taken_by_student_id = 2433;
select * from marks join subjects on marks.id = subjects.id;
select books.title book_title, marks.mark mark_number, lessons.title lesson_title, students.group_id group_number from students
JOIN books on students.id = books.taken_by_student_id
JOIN marks on students.id = marks.student_id
JOIN lessons on marks.lesson_id = lessons.id
JOIN `groups` on students.group_id = `groups`.id
WHERE students.id = 2433;