"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from job.views import getJobs, getJob, createJob, updateJob, deleteJob, getTopicStats
from account.views import register, current_user

# Build in
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/jobs/", getJobs, name="jobs"),
    path("api/jobs/<str:id>/", getJob, name="job"),
    path("api/jobs/new", createJob, name="create-job"),
    path("api/jobs/update/<str:id>/", updateJob, name="update-job"),
    path("api/jobs/delete/<str:id>/", deleteJob, name="delete-job"),
    path("api/stats/<str:topic>/", getTopicStats, name="jobs-by-topic"),
    path("api/auth/register", register, name="register"),
    # Build in LOGIN functionality. In Response token is set in cookies
    path("api/auth/token", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("api/token/verify", TokenVerifyView.as_view()),
    path("api/me/", current_user, name="current-user"),
]
