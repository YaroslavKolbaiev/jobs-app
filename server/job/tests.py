from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from django.core.files.storage import FileSystemStorage
from django.test import TestCase
from django.urls import reverse
from job.models import CandidatesApplied, Job
import json
from datetime import datetime
from django.contrib.auth.models import User


def mockFn():
    print("Hello Mock")
    return FileSystemStorage


class JobViewTestCase(TestCase):
    def setUp(self):
        self.create_job(title="React Developer", salary=120000, industry="IT")
        self.create_job(title="Manager", salary=30000, industry="Banking")

    def test_get_all_jobs_filter_industry(self):
        response = self.client.get(reverse("jobs") + "?industry=IT")
        jobs = response.json()["jobs"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(jobs), 1)
        for job in jobs:
            self.assertEqual(job["industry"], "IT")

    def test_get_all_jobs_filter_salary(self):
        response = self.client.get(reverse("jobs") + "?min_salary=40000")
        self.assertEqual(response.status_code, 200)

    def test_get_all_jobs_filter_title(self):
        response = self.client.get(reverse("jobs") + "?keyword=react")
        jobs = response.json()["jobs"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(jobs), 1)
        for job in jobs:
            self.assertEqual(job["industry"], "IT")

    def test_create_job(self):
        response = self.create_job(title="Java Developer", salary=30000, industry="IT")

        title = response["response_data"].json()["title"]
        salary = response["response_data"].json()["salary"]

        self.assertEqual(title, title)
        self.assertEqual(salary, salary)

    @patch("storages.backends.s3boto3.S3Boto3Storage", new_callable=mockFn)
    def test_apply_job(self, mock_apply_job):
        related_job = self.create_job(
            title="Mechanoc", salary=45000, industry="Telecommunication"
        )
        job_id = related_job["response_data"].json()["id"]
        token = related_job["token"]
        user_id = related_job["response_data"].json()["user"]

        user = User.objects.get(id=user_id)

        file = SimpleUploadedFile("file.doc", b"file_content")

        user.__getattribute__("userprofile").resume = file
        user.__getattribute__("userprofile").save()

        url = reverse("apply-job", kwargs={"job_id": job_id})

        # Add the token to the request headers
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.post(
            url,
            content_type="application/json",
            headers=headers,  # type: ignore
        )

        res_data = response.json()

        job_applied = CandidatesApplied.objects.get(job=job_id)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(res_data["job"], job_id)
        self.assertEqual(job_applied.resume, res_data["resume"])

    def test_get_topic_stats(self):
        query = "React"
        url = reverse("jobs-by-topic", kwargs={"topic": query})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_update_job(self):
        job_to_update = self.create_job(
            title="Driver", salary=25000, industry="Telecommunication"
        )

        job_id = job_to_update["response_data"].json()["id"]

        url = reverse(
            "update-job", kwargs={"id": job_id}
        )  # replace with the actual name of the url
        data = {
            "title": "Job1 Updated",
            "description": "Updated description",
            "email": "test@gmail.com",
            "address": "test address",
            "salary": 10000,
            "position": 1,
            "company": "test company",
            "point": "POINT(0.0 0.0)",
            "lastDate": "2024-03-20T04:30:50.992728Z",
            "user": None,
            "created_at": datetime.now().isoformat(),
            "jobType": "Permanent",
            "education": "Bachelor",
            "industry": "IT",
            "experience": "No Experience",
        }

        token = job_to_update["token"]

        # Add the token to the request headers
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.put(
            url,
            data=json.dumps(data),
            content_type="application/json",
            headers=headers,  # type: ignore
        )

        updated_job = self.get_job_by_id(job_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_job["title"], data["title"])
        self.assertEqual(updated_job["description"], data["description"])

    def test_delete_job(self):
        job_to_delete = self.create_job(
            title="Call Manager", salary=25000, industry="Telecommunication"
        )

        token = job_to_delete["token"]
        job_id = job_to_delete["response_data"].json()["id"]

        url = reverse("delete-job", kwargs={"id": job_id})
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.delete(
            url,
            content_type="application/json",
            headers=headers,  # type: ignore
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Job.objects.filter(id=job_id).exists(), False)

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

    def create_job(self, title: str, salary: int, industry: str):
        url = reverse("create-job")
        data = {
            "title": title,
            "description": "Job description",
            "email": "test@gmail.com",
            "address": "test address",
            "salary": salary,
            "position": 1,
            "company": "test company",
            "point": "POINT(0.0 0.0)",
            # "lastDate": "2024-02-02",  # this is created automatically if not provided
            "user": None,
            # "created_at": "2024-02-02", # this is created automatically if not provided
            "jobType": "Permanent",
            "education": "Bachelor",
            "industry": industry,
            "experience": "No Experience",
        }

        token = self.get_token()

        # Add the token to the request headers
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
            headers=headers,  # type: ignore
        )

        return {"response_data": response, "token": token}

    def get_job_by_id(self, id):
        response = self.client.get(reverse("job", kwargs={"id": id}))

        return response.json()
