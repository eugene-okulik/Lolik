INSERT INTO students (name, second_name) 
values ('Maria', 'Ivanova')

INSERT INTO books (title, taken_by_student_id)
Values 	('Distributed motivating installation644', '3467'),
('DOpen-source disintermediate strategy 8', '3467'),
('Visionary object-oriented moratorium', '3467')

INSERT INTO `groups`  (title, start_date, end_date)
Values ('OM', '18.02.1993', '24/05/2024')

UPDATE  students   SET group_id = '2162'
where id = '3467' or id = '3467'

INSERT INTO subjets  (title)
Values ('Maths in Enlish'), ('Birth or Die'), ('Hello World')

INSERT INTO lessons  (title, subject_id)
Values ('Maths', '3170'), ('Litherature', '3172'), ('Russian lang', '3173'), 
('Maths for child', '3170'), ('Litherature for child', '3172'), ('Russian lang for child', '3173')

INSERT INTO marks  (value, lesson_id, student_id)
Values ('A', '6512', '3467'), ('B', '6513', '3467'), ('C', '6514', '3467'), 
('A+','6515', '3467'), ('B-', '6516', '3467'), ('C+', '6517', '3467')

SELECT * from marks m 
where student_id = '3467'

SELECT * from books b 
WHERE taken_by_student_id = '3467'

SELECT s.id, s.name, s.second_name, g.id as group_id, g.title as title_group, 
       b.title as taken_books, m.value as mark, sub.title as subject_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id 
LEFT JOIN subjets sub ON l.subject_id  = sub.id  
WHERE s.id = '3467'
GROUP BY s.id, s.name, s.second_name, g.id, g.title, b.title, m.value, sub.title

