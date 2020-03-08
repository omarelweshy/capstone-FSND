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

  # DELETE teacher
  @app.route('/delete_teacher/<int:id>', methods=['GET' ,'DELETE'])
  def delete_teacher(id):
    teacher = Teacher.query.filter(Teacher.id == id).one_or_none()
    teacher.delete()
    return render_template('pages/teacher_delete_success.html')

  # DELETE student
  @app.route('/delete_student/<int:id>', methods=['GET' ,'DELETE'])
  def delete_student(id):
    student = Student.query.filter(Student.id == id).one_or_none()
    student.delete()
    return render_template('pages/student_delete_success.html')

  # PATCH teacher
  @app.route('/teachers/<int:teacher_id>', methods=['GET', 'PATCH'])
  def edit_teacher(teacher_id):
    return render_template("forms/edit_teacher.html")

  # PATCH student
  @app.route('/edit_student')
  def edit_student():
    return render_template("forms/edit_student.html")


  @app.errorhandler(404)
  def not_found_error(error):
      return render_template('errors/404.html'), 404

  @app.errorhandler(500)
  def server_error(error):
      return render_template('errors/500.html'), 500
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)