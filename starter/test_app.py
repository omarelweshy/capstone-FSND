import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Teacher, Student


class SchoolTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "school"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'omar',
            '010',
            'localhost:5432',
            self.database_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_teachers_200(self):
        req = self.client().get('/teachers')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_get_students_200(self):
        req = self.client().get('/students')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_teachers_200(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().post('/teachers', json=teacher)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_teachers_422(self):
        teacher = {
            'phone': 'Any Number'
        }
        req = self.client().post('/teachers', json=teacher)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)

    def test_post_students_200(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().post('/students', json=student)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_students_422(self):
        student = {
            'phone': 'Any Number'
        }
        req = self.client().post('/students', json=student)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)

    def test_delete_teachers_200(self):
        req = self.client().delete('/teachers/5')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_delete_students_200(self):
        req = self.client().delete('/students/5')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_delete_teachers_422(self):
        req = self.client().delete('/teachers/10000')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)

    def test_delete_students_422(self):
        req = self.client().delete('/students/10000')
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)

    def test_patch_teachers_200(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().patch('/teachers/4', json=teacher)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_patch_students_200(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().patch('/students/11', json=student)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_patch_teachers_422(self):
        teacher = {
            'phone': 'Any num'
        }
        req = self.client().patch('/teachers/11', json=teacher)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)

    def test_patch_students_422(self):
        student = {
            'phone': 'Any num'
        }
        req = self.client().patch('/students/11', json=student)
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 422)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
