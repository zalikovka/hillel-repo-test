from unittest import TestCase
from app import app


class TestApi(TestCase):
    def setUp(self) -> None:
        # set up flast test client
        self.client = app.test_client()

    def test_api_get_students(self):
        # send request to /students
        response = self.client.get("/students")

        # check status code
        self.assertEqual(response.status_code, 200)

    def test_api_get_marks(self):
        # send request to /students
        response = self.client.get("/marks")

        # check status code
        self.assertEqual(response.status_code, 200)

    def test_api_create_student_negative_age(self):
        # send request to /students
        response = self.client.post("/students", json={
            "name": "Nataliia",
            "age": -1
        })

        # check status code
        self.assertEqual(response.status_code, 422)

    def test_api_create_student_no_data(self):
        # send request to /students
        response = self.client.post("/students", json={
        })

        # check status code
        self.assertEqual(response.status_code, 422)

    def test_api_create_student(self):
        # send request to /students
        response = self.client.post("/students", json={
            "name": "Nataliia",
            "age": 25
        })

        # check status code
        self.assertEqual(response.status_code, 201)
