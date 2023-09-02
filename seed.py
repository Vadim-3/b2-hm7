from faker import Faker
from src.models import session, Student, Subject, Teacher, Grade, Group
from random import randint, choice
from datetime import date
fake_data = Faker()

fake_groups = [fake_data.company() for _ in range(3)]
groups = []
for g in fake_groups:
    group = Group(group_name=g)
    groups.append(group)
    session.add(group)

fake_teachers = [fake_data.name() for _ in range(5)]
teachers = []
for t in fake_teachers:
    teacher = Teacher(teacher_name=t)
    teachers.append(teacher)
    session.add(teacher)

fake_subjects = ['English', 'physics', 'chemistry',
                 'math', 'Ukrainian language', 'geography', 'history']
subjects = []
for name in fake_subjects:
    subject = Subject(name=name, teacher=choice(teachers))
    subjects.append(subject)
    session.add(subject)

fake_students = [fake_data.name() for _ in range(30)]
students = []
for i in fake_students:
    student = Student(student_name=i, group=choice(groups))
    students.append(student)
    session.add(student)
    for subject in subjects:
        num_of_grades = randint(1, 20)
        for _ in range(num_of_grades):
            grade = Grade(grade=randint(1, 12), subject=subject,
                          student=student, date=fake_data.date_between(start_date=date(2022, 9, 1), end_date=date(2023, 5, 31)))
            session.add(grade)

session.commit()
grades = session.query(Grade).all()
for grade in grades:
    print(f"grade:{grade.grade}, student:{grade.student.student_name}, subject:{grade.subject.name}, date:{grade.date}")