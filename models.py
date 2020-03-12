# importing
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
import json

# database setting
database_name = "school"
# database_path = "postgresql://{}:{}@{}/{}".format(
#     'omar', '010', 'localhost:5432', database_name)
database_path = os.getenv("DATABASE_URL")

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Models

# Teacher


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Student


class Student(db.Model):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
