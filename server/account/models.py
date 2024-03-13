from django.db import models
from django.contrib.auth.models import User


# Create UserProfile models here.
class UserProfile(models.Model):
    # Define one to one relationship with the user model
    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )
    # Resume fieled is for the user to upload their resume
    resume = models.FileField(null=True)
