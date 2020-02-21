import os
from flask import Flask, request, abort, jsonify, render_template, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Teacher, Student

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def index():
    return render_template("pages/home.html")

  # GET teachers
  @app.route('/teachers', methods=['GET'])
  def get_teachers():
    teachers = Teacher.query.all()
    return render_template("pages/teachers.html", teachers=teachers)

  # GET students
  @app.route('/students')
  def get_students():
    students = Student.query.all()
    return render_template("pages/students.html", students=students)


  # POST teacher
  @app.route('/create_teacher', methods=['GET','POST'])
  def create_teacher():
    if request.method == 'POST':
      name = request.form['name']
      address = request.form['address']
      phone = request.form['phone']
      teacher = Teacher(
        name=name,
        address=address,
        phone=phone
      )
      teacher.insert()
    return render_template("forms/create_teacher.html")

  # POST student
  @app.route('/create_student', methods=['GET','POST',])
  def create_student():
    if request.method == 'POST':
      name = request.form['name']
      address = request.form['address']
      phone = request.form['phone']
      student = Student(
        name=name,
        address=address,
        phone=phone
      )
      student.insert()
    return render_template("forms/create_student.html")


  # PATCH teacher
  @app.route('/edit_teacher')
  def edit_teacher():
    return render_template("forms/edit_teacher.html")

  # PATCH student
  @app.route('/edit_student')
  def edit_student():
    return render_template("forms/edit_student.html")


  # DELETE teacher
  @app.route('/delete_teacher/<id>', methods=['DELETE'])
  def delete_teacher(id):
    teacher = Teacher.query.filter_by(id=id).one_or_none()
    teacher.delete()
    return None

  # DELETE student
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)