from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User


# Create your tests here.
class AccountViewTestCase(TestCase):
    global EXISTED_USER
    EXISTED_USER = {
        "first_name": "test_name",
        "last_name": "test_last_name",
        "email": "test@gmail.com",
        "password": "test_password",
        "username": "test_username",
    }

    def setUp(self):
        self.client = Client()
        self.create_user()

    def create_user(self):
        User.objects.create(
            first_name=EXISTED_USER["first_name"],
            last_name=EXISTED_USER["last_name"],
            email=EXISTED_USER["email"],
            password=EXISTED_USER["password"],
            username=EXISTED_USER["username"],
        )

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
            "first_name": "test_name2",
            "last_name": "test_last_name2",
            "email": EXISTED_USER["email"],
            "password": "test_password",
            "username": "test_username2",
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
