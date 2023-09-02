from src.models import session, Student, Subject, Group, Teacher
from random import randint
import argparse


def create(model, name):
    if model.lower() == "student":
        student = Student(student_name=name, group_id=randint(1, 3))
        session.add(student)
        session.commit()
    elif model.lower() == "teacher":
        teacher = Teacher(teacher_name=name)
        session.add(teacher)
        session.commit()
    elif model.lower() == "subject":
        subject = Subject(name=name, teacher_id=randint(1, 5))
        session.add(subject)
        session.commit()
    elif model.lower() == "group":
        group = Group(group_name=name)
        session.add(group)
        session.commit()


def update(model, id, name):
    if model.lower() == "student":
        student = session.query(Student).get(id)
        student.student_name = name
        session.add(student)
        session.commit()
    elif model.lower() == "teacher":
        teacher = session.query(Teacher).get(id)
        teacher.teacher_name = name
        session.add(teacher)
        session.commit()
    elif model.lower() == "subject":
        subject = session.query(Subject).get(id)
        subject.name = name
        session.add(subject)
        session.commit()
    elif model.lower() == "group":
        group = session.query(Group).get(id)
        group.group_name = name
        session.add(group)
        session.commit()


def list(model, id=None):
    if id == None:
        if model.lower() == "student":
            students = session.query(Student).all()
            students_names = [name.student_name for name in students]
            print(students_names)
        elif model.lower() == "teacher":
            teachers = session.query(Teacher).all()
            teachers_names = [name.teacher_name for name in teachers]
            print(teachers_names)
        elif model.lower() == "subject":
            subjects = session.query(Subject).all()
            subjects_names = [name.name for name in subjects]
            print(subjects_names)
        elif model.lower() == "group":
            groups = session.query(Group).all()
            groups_names = [name.group_name for name in groups]
            print(groups_names)
    else:
        if model.lower() == "student":
            student = session.query(Student).get(id)
            print(student.id, student.student_name)
        elif model.lower() == "teacher":
            teacher = session.query(Teacher).get(id)
            print(teacher.id, teacher.teacher_name)
        elif model.lower() == "subject":
            subject = session.query(Subject).get(id)
            print(subject.id, subject.name)
        elif model.lower() == "group":
            group = session.query(Group).get(id)
            print(group.id, group.group_name)


def remove(model, id):
    if model.lower() == "student":
        student = session.query(Student).get(id)
        session.delete(student)
        session.commit()
    elif model.lower() == "teacher":
        teacher = session.query(Teacher).get(id)
        session.delete(teacher)
        session.commit()
    elif model.lower() == "subject":
        subject = session.query(Subject).get(id)
        session.delete(subject)
        session.commit()
    elif model.lower() == "group":
        group = session.query(Group).get(id)
        session.delete(group)
        session.commit()


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", type=str)
parser.add_argument("-m", "--model", type=str)
parser.add_argument("-n", "--name", type=str)
parser.add_argument("--id", type=int)

args = parser.parse_args()

if args.action == "create":
    create(model=args.model, name=args.name)
elif args.action == "remove":
    remove(model=args.model, id=args.id)
elif args.action == "update":
    update(model=args.model, id=args.id, name=args.name)
elif args.action == "list":
    list(model=args.model, id=args.id)
else:
    raise ValueError()