from datetime import datetime, timedelta
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import os
import geocoder


def return_default_date():
    now = datetime.now()
    return now + timedelta(days=10)  # 10 days from now


# Create models
class JobType(models.TextChoices):
    Permanent = "Permanent"
    Contract = "Contract"
    Internship = "Internship"
    Temporary = "Temporary"


class Education(models.TextChoices):
    Bachelor = "Bachelor"
    Master = "Master"
    PhD = "PhD"


class Experience(models.TextChoices):
    NO_EXPERIENCE = "No Experience"
    ONE_YEAR = "1 Year"
    TWO_YEARS = "2 Years"
    THREE_YEARS = "3 Years"


class Industry(models.TextChoices):
    IT = "IT"
    Business = "Business"
    Banking = "Banking"
    Education = "Education"
    Telecommunication = "Telecommunication"
    Others = "Others"


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    email = models.EmailField()
    address = models.CharField(max_length=200, null=True)
    salary = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000000)]
    )
    position = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_default_date)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )  # User is from django.contrib.auth.models
    created_at = models.DateTimeField(auto_now_add=True)
    jobType = models.CharField(
        max_length=100, choices=JobType.choices, default=JobType.Permanent
    )
    education = models.CharField(
        max_length=100, choices=Education.choices, default=Education.Bachelor
    )
    industry = models.CharField(
        max_length=100, choices=Industry.choices, default=Industry.Others
    )
    experience = models.CharField(
        max_length=100, choices=Experience.choices, default=Experience.NO_EXPERIENCE
    )

    # The save function is a method defined within the Job class.
    # It overrides the default save method provided by Django's Model class,
    # allowing you to customize the saving behavior of Job objects.
    def save(self, *args, **kwargs):
        g = geocoder.mapquest(self.address, key=os.environ.get("GEOCODER_API"))
        lng = g.lng
        lat = g.lat
        self.point = Point(lng, lat)
        # This ensures that whenever a Job object is saved,
        # the point attribute is automatically updated based on the provided address.
        super(Job, self).save(*args, **kwargs)
