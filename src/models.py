from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped, declarative_base
from datetime import datetime
import psycopg2

DATABASE_URL = "postgresql+psycopg2://postgres:12345678qwerty@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(250), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="CASCADE"))
    group = relationship(Group, backref="students")


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(250), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete="CASCADE"))
    teacher = relationship(Teacher, backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    student = relationship(Student, backref="grades")
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    subject = relationship(Subject, backref="grades")


Base.metadata.bind = engine