import os
from flask import Flask, request, abort, jsonify, render_template, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from models import setup_db, Teacher, Student
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add(
          "Access-Control-Allow-Headers",
          "Content-Type,Authorization,true")
      response.headers.add(
          "Access-Control-Allow-Methods",
          "GET, PATCH, POST, DELETE")
      return response

  # GET teachers
  @app.route('/teachers', methods=['GET'])
  @requires_auth('get:teachers')
  def get_teachers(payload):
    try:
      teachers = Teacher.query.all()
      formatted_teachers = {teacher.id: teacher.name for teacher in teachers}
      return jsonify ({
        'tearcher': formatted_teachers,
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # GET students
  @app.route('/students')
  @requires_auth('get:students')
  def get_students(payload):
    try:
      students = Student.query.all()
      formatted_students = {student.id: student.name for student in students}
      return jsonify ({
        'students': formatted_students,
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # POST teacher
  @app.route('/teachers', methods=['POST'])
  @requires_auth('post:teachers')
  def create_teacher(payload):
    try:
      body = request.get_json()
      name = body.get('name')
      teacher = Teacher(name=name)
      teacher.insert()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # POST student
  @app.route('/students', methods=['POST'])
  @requires_auth('post:students')
  def create_student(payload):
    try:
      body = request.get_json()
      name = body.get('name')
      student = Student(name=name)
      student.insert()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # DELETE teacher
  @app.route('/teachers/<int:id>', methods=['DELETE'])
  @requires_auth('delete:teachers')
  def delete_teacher(payload, id):
    try:
      teacher = Teacher.query.filter(Teacher.id == id).one_or_none()
      teacher.delete()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # DELETE student
  @app.route('/students/<int:id>', methods=['DELETE'])
  @requires_auth('delete:students')
  def delete_student(payload, id):
    try:
      student = Student.query.filter(Student.id == id).one_or_none()
      student.delete()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # PATCH teacher
  @app.route('/teachers/<int:id>', methods=['PATCH'])
  @requires_auth('patch:teachers')
  def edit_teacher(payload, id):
    try:
      teacher = Teacher.query.filter_by(id=id).one_or_none()
      body = request.get_json()
      new_name = body["name"]
      teacher.name = new_name
      teacher.update()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # PATCH student
  @app.route('/students/<int:id>', methods=['PATCH'])
  @requires_auth('patch:students')
  def edit_student(payload, id):
    try:
      student = Student.query.filter_by(id=id).one_or_none()
      body = request.get_json()
      new_name = body["name"]
      student.name = new_name
      student.update()
      return jsonify ({
        'success': True,
        'status_code': 200
      })
    except Exception:
        abort(422)

  # ERROR handlers
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad request"
      }), 400

  @app.errorhandler(405)
  def method_not_allow(error):
      return jsonify({
          "success": False,
          "error": 405,
          "message": "Method not allow"
      }), 405

  @app.errorhandler(AuthError)
  def auth_error(auth_error):
      return jsonify({
          "success": False,
          "error": auth_error.status_code,
          "message": auth_error.error['description']
      }), auth_error.status_code
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)