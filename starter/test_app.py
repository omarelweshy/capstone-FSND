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


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
