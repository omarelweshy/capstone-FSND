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
        # TOKEN get pip 8 style Guide and Failure because of permissions in Test, When you change it, it will work..
        self.token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VRkVSVVl4UTBFNFFUY3lSRGd4UkRrd01qRXdNemhHUVRGQ1JVRkdNRU13UkRFek1qUTROZyJ9.eyJpc3MiOiJodHRwczovL29tYXJjYXAuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNjc3YjlhNjBhY2FhMGQ3ZGVhYzY4NyIsImF1ZCI6InNjaG9vbCIsImlhdCI6MTU4NDAyMzA4OCwiZXhwIjoxNTg0MDMwMjg4LCJhenAiOiI4NGZIS0w5bVhudlVGdjJqMFlLeHRQdGRNUjVFaHM0SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnN0dWRlbnRzIiwiZGVsZXRlOnRlYWNoZXJzIiwiZ2V0OnN0dWRlbnRzIiwiZ2V0OnRlYWNoZXJzIiwicGF0Y2g6c3R1ZGVudHMiLCJwYXRjaDp0ZWFjaGVycyIsInBvc3Q6c3R1ZGVudHMiLCJwb3N0OnRlYWNoZXJzIl19.AcHRlBasEnk-bbp9sdxIgTdmwe_LMZiPsJ1nJQF5B2MjNjfBdj129Wl_JTilvkr-IfbVj88m9AalEUHEea6rEFuCyM_wfO3sbnvR6lNy1X5lPyPQbrL8IMTATeR0QSbrZtw2DnySCK-TEg_tV1C0xRELYKyTAS_1448fkvp1wf4t0mzHzGfXDKK9GxyOjRBJl4zV7asx6NmeX1yyO0Y475UVrEVw6KEild69inrZ9rXmCPRmHmbc20i6kzB0MEXyb5dXI0F-Bc7kNjt7e_OrHCk_ppP_6Q8Ox-w6awgmjbH78C6Eu7yrZ-JnwEY6Hw1bbYyOTg2g_EZaL_6gGN87yw"
        #self.database_name = "school_test"
        self.database_path = database_path = os.getenv("DATABASE_URL")
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
        req = self.client().get(
            '/teachers',
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_get_students_200(self):
        req = self.client().get(
            '/students',
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_teachers_200(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().post(
            '/teachers',
            json=teacher,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_teachers_401(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().post(
            '/teachers',
            json=teacher,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)

    def test_post_students_200(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().post(
            '/students',
            json=student,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_post_students_401(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().post(
            '/students',
            json=student,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)

    def test_delete_teachers_200(self):
        req = self.client().delete('/teachers/5',
                                   headers={
                                       'Authorization': 'Bearer ' + self.token
                                    })
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_delete_students_200(self):
        req = self.client().delete('/students/7',
                                   headers={
                                       'Authorization': 'Bearer ' + self.token
                                       })
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_delete_teachers_401(self):
        req = self.client().delete('/teachers/10000',
                                   headers={
                                       'Authorization': 'Bearer ' + self.token
                                       })
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)

    def test_delete_students_401(self):
        req = self.client().delete('/students/10000',
                                   headers={
                                       'Authorization': 'Bearer ' + self.token
                                       })
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)

    def test_patch_teachers_200(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().patch(
            '/teachers/4',
            json=teacher,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_patch_students_200(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().patch(
            '/students/11',
            json=student,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 200)

    def test_patch_teachers_401(self):
        teacher = {
            'name': 'Any name'
        }
        req = self.client().patch(
            '/teachers/11',
            json=teacher,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)

    def test_patch_students_401(self):
        student = {
            'name': 'Any name'
        }
        req = self.client().patch(
            '/students/11',
            json=student,
            headers={
                'Authorization': 'Bearer ' + self.token})
        data = json.loads(req.data)
        self.assertEqual(req.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
