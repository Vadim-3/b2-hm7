from sqlalchemy import func, desc, select, and_
from src.models import Teacher, Student, Subject, Grade, Group, session


def query_one():
    result = session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def query_two(subject_id: int):
    result = session.query(Subject.name, Student.student_name,
                           func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id == subject_id).group_by(Student.id, Subject.name).order_by(desc('avg_grade')).limit(1).all()
    return result


def query_three(subject_id: int):
    result = session.query(Group.group_name, func.round(func.avg(
        Grade.grade), 2).label('average_grade')).join(Student, Group.id == Student.group_id).join(Grade, Student.id == Grade.student_id).filter(Grade.subject_id == subject_id).group_by(Group.group_name).order_by(func.avg(Grade.grade).desc()).all()
    return result


def query_four():
    result = session.query(Student.student_name, func.round(
        func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
    return result


def query_five(teacher_id: int):
    result = session.query(Teacher.teacher_name,
                           Subject.name).join(Subject).filter(Teacher.id == teacher_id).all()
    return result


def query_six(group_id: int):
    result = session.query(Student.student_name, Group.group_name).join(
        Group).filter(Group.id == group_id).all()
    return result


def query_seven(group_id: int, subject_id: int):
    result = session.query(Student.student_name, Subject.name, Grade.grade).join(Grade.student).join(Grade.subject).join(
        Student.group).filter(Group.id == group_id).filter(Subject.id == subject_id).all()
    return result


def query_eight(teacher_id: int):
    result = session.query(Teacher.teacher_name, func.round(func.avg(
        Grade.grade), 2).label('avg_grade')).join(Subject, Teacher.id == Subject.teacher_id).join(Grade, Subject.id == Grade.subject_id).filter(Teacher.id == teacher_id).group_by(Teacher.teacher_name).first()
    return result


def query_nine(student_id: int):
    result = session.query(Subject.name, Student.student_name).join(Grade, Student.id == Grade.student_id).join(
        Subject, Subject.id == Grade.subject_id).filter(Student.id == student_id).distinct().all()
    return result


def query_ten(student_id: int, teacher_id: int):
    result = session.query(Student.student_name,
                           Teacher.teacher_name, Subject.name).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).join(Teacher, Teacher.id == Subject.teacher_id).filter(Student.id == student_id, Teacher.id == teacher_id).distinct().all()
    return result


def query_eleven(student_id: int, teacher_id: int):
    result = session.query(Student.student_name, Teacher.teacher_name, func.round(
        func.avg(Grade.grade), 2).label('avg_grade')).join(Subject, Teacher.id == Subject.teacher_id).join(Grade, Subject.id == Grade.subject_id).join(Student, Grade.student_id == Student.id).filter(Student.id == student_id, Teacher.id == teacher_id).group_by(Teacher.teacher_name, Student.student_name).first()
    return result


def query_twelve(group_id: int, subject_id: int):
    result = session.query(Group.group_name, Subject.name, Student.student_name, Grade.grade).join(
        Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).join(Group, Student.group_id == Group.id).filter(Group.id == group_id, Subject.id == subject_id).order_by(desc(Grade.date)).limit(1).all()
    return result


print(query_one())
print(query_two(4))
print(query_three(4))
print(query_four())
print(query_five(4))
print(query_six(2))
print(query_seven(2, 1))
print(query_eight(4))
print(query_nine(1))
print(query_ten(1, 1))
print(query_eleven(1, 1))
print(query_twelve(1, 1))