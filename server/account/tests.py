from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User

DEFAULT_USER = {
    "first_name": "test_name",
    "last_name": "test_last_name",
    "email": "tes2@gmail.com",
    "password": "test_password",
    "username": "test_username",
}


def sign_up():
    Client().post(
        reverse("register"),
        data=json.dumps(DEFAULT_USER),
        content_type="application/json",
    )


# Create your tests here.
class AccountViewTestCase(TestCase):
    def setUp(self):
        sign_up()

    def test_register(self):
        data = {
            "first_name": "test_name2",
            "last_name": "test_last_name2",
            "email": "test2@gmail.com",
            "password": "test_password",
            "username": "test_username2",
        }
        response = self.client.post(
            reverse("register"),
            data=json.dumps(data),
            content_type="application/json",
        )

        # check if response is 201
        self.assertEqual(response.status_code, 201)
        # check if the user is created
        self.assertEqual(response.json()["message"], "User registered")

    def test_register_email_exists(self):
        data = {
            "first_name": "test_name3",
            "last_name": "test_last_name3",
            "email": DEFAULT_USER["email"],
            "password": "test_password",
            "username": "test_username3",
        }

        response = self.client.post(
            reverse("register"),
            data=json.dumps(data),
            content_type="application/json",
        )

        # check if response is 400
        self.assertEqual(response.status_code, 400)
        # check if message is "Email already exists"
        self.assertEqual(response.json()["message"], "Email already exists")

    def test_register_short_password(self):
        data = {
            "first_name": "test_name23",
            "last_name": "test_last_name23",
            "email": "test23@gmail.com",
            "password": "test",
            "username": "test_username23",
        }
        response = self.client.post(
            reverse("register"),
            data=json.dumps(data),
            content_type="application/json",
        )

        # check if response is 400
        self.assertEqual(response.status_code, 400)
        # check if message is "Password must be at least 6 characters"
        self.assertEqual(
            response.json()["password"][0],
            "Ensure this field has at least 6 characters.",
        )

    def test_login(self):
        data = {
            "password": DEFAULT_USER["password"],
            "username": DEFAULT_USER["username"],
        }

        response = self.client.post(
            reverse("token-obtain-pair"),
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        # Check if response data contains kyes refresh and access
        self.assertIn("refresh", response.json())
        self.assertIn("access", response.json())
