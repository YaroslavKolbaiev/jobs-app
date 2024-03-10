from django.test import TestCase, Client
from django.urls import reverse
from job.models import Job
import json
from datetime import datetime


class JobViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.job1 = Job.objects.create(
            title="Job-Default",
            description="Job-default description",
            email="test-default@gmail.com",
            address="test address",
            salary=1000,
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
            title="Job-Default2",
            description="Job-default2 description",
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
            industry="IT",
            experience="No Experience",
        )

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

    def test_update_job(self):
        job_to_update = Job.objects.get(id=1)
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

    def test_get_topic_stats(self):
        url = reverse("jobs-by-topic", kwargs={"topic": "Job"})
        response = self.client.get(url)

        if response.status_code == 404:
            return self.assertEqual(
                response.json()["message"], "No job found for React"
            )

        self.assertEqual(response.status_code, 200)
