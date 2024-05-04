from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


# Create UserProfile models here.
class UserProfile(models.Model):
    # Define one to one relationship with the user model. related_name is reference used in UserSerializer
    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )
    # Resume fieled is for the user to upload their resume
    resume = models.FileField(null=True)


# In Django, signals are a way to allow decoupled applications to get
# notified when certain actions occur. Signals are sent by senders and
# received by receivers. The post_save signal is sent after a model's
# instance is saved(in this case when user.userprofile.save() runs in upload_resume view)
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance

    if created:
        profile = UserProfile(user=user)
        profile.save()
