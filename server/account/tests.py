from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

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


def mockFn(self):
    print("Hello Mock")


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

    def test_update_user(self):
        new_useername = "updated_user_name"
        new_email = "new-email-is-good@gmail.com"
        new_first_name = "new_first_name"
        new_last_name = "new_last_name"
        data = {
            "username": new_useername,
            "email": new_email,
            "first_name": new_first_name,
            "last_name": new_last_name,
        }

        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.put(
            reverse("update-user"),
            data=json.dumps(data),
            content_type="application/json",
            headers=headers,  # type: ignore
        )

        user_id = response.json()["user_id"]

        user = User.objects.get(id=user_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.username, new_useername)
        self.assertEqual(user.email, new_email)
        self.assertEqual(user.first_name, new_first_name)
        self.assertEqual(user.last_name, new_last_name)

    def get_token(self):
        sign_up_data = {
            "first_name": "test_name",
            "last_name": "test_last_name",
            "email": "tes2@gmail.com",
            "password": "test_password",
            "username": "test_username",
        }
        self.client.post(
            reverse("register"),
            data=json.dumps(sign_up_data),
            content_type="application/json",
        )

        data = {
            "password": sign_up_data["password"],
            "username": sign_up_data["username"],
        }

        response = self.client.post(
            reverse("token-obtain-pair"),
            data=json.dumps(data),
            content_type="application/json",
        )

        return response.json()["access"]

    @patch("account.models.UserProfile.save", mockFn)
    def test_upload_resume(self):
        file = SimpleUploadedFile("file.doc", b"file_content")

        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.post(
            reverse("upload-resume"),
            data={"resume": file},
            format="multipart",
            headers=headers,  # type: ignore
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["resume"], file.name)

    def test_upload_resume_invalid_extension(self):
        file = SimpleUploadedFile("file.txt", b"file_content")

        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.post(
            reverse("upload-resume"),
            data={"resume": file},
            format="multipart",
            headers=headers,  # type: ignore
        )

        self.assertEqual(response.status_code, 404)
