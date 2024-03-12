from django.test import TestCase, Client
from django.urls import reverse
from job.models import Job
import json
from datetime import datetime
from django.contrib.auth.models import User


class JobViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.job1 = Job.objects.create(
            title="React Developer",
            description="React developer description",
            email="test-default@gmail.com",
            address="test address",
            salary=10000,
            position=1,
            company="test company",
            point="POINT(0.0 0.0)",
            user=None,
            created_at=datetime.now().isoformat(),
            jobType="Permanent",
            education="Bachelor",
            industry="IT",
            experience="No Experience",
        )
        self.job2 = Job.objects.create(
            title="Manager",
            description="Job driver description",
            email="test@gmail.com",
            address="test address",
            salary=50000,
            position=1,
            company="test company2",
            point="POINT(0.0 0.0)",
            user=None,
            created_at=datetime.now().isoformat(),
            jobType="Permanent",
            education="PhD",
            industry="Telecommunication",
            experience="No Experience",
        )

    def test_get_all_jobs_filter_industry(self):
        response = self.client.get(reverse("jobs") + "?industry=IT")
        jobs = response.json()["jobs"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(jobs), 1)
        for job in jobs:
            self.assertEqual(job["industry"], "IT")

    def test_get_all_jobs_filter_salary(self):
        response = self.client.get(reverse("jobs") + "?min_salary=40000")
        jobs = response.json()["jobs"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(jobs), 1)
        for job in jobs:
            self.assertGreater(job["salary"], 40000)

    def test_get_all_jobs_filter_title(self):
        response = self.client.get(reverse("jobs") + "?keyword=react")
        jobs = response.json()["jobs"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(jobs), 1)
        for job in jobs:
            self.assertEqual(job["industry"], "IT")

    def test_create_job(self):
        url = reverse("create-job")
        data = {
            "title": "Job1",
            "description": "Job1 description",
            "email": "test@gmail.com",
            "address": "test address",
            "salary": 10000,
            "position": 1,
            "company": "test company",
            "point": "POINT(0.0 0.0)",
            # "lastDate": "2024-02-02",  # this is created automatically if not provided
            "user": None,
            # "created_at": "2024-02-02", # this is created automatically if not provided
            "jobType": "Permanent",
            "education": "Bachelor",
            "industry": "IT",
            "experience": "No Experience",
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )

        title = response.json()["title"]
        salary = response.json()["salary"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(title, "Job1")
        self.assertEqual(salary, 10000)

    def test_get_topic_stats(self):
        query = "Job"
        url = reverse("jobs-by-topic", kwargs={"topic": query})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_update_job(self):
        job_to_update = Job.objects.get(id=1)
        print("JOB TO UPDATE:", job_to_update)
        url = reverse(
            "update-job", kwargs={"id": job_to_update.pk}
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
        response = self.client.put(
            url, data=json.dumps(data), content_type="application/json"
        )

        updated_job = Job.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_job.title, data["title"])
        self.assertEqual(updated_job.description, data["description"])

    def test_delete_job(self):
        id = self.job1.pk
        url = reverse("delete-job", kwargs={"id": id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Job.objects.filter(id=id).exists(), False)


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
