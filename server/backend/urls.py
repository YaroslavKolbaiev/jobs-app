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
from job.views import (
    getJobs,
    getJob,
    createJob,
    updateJob,
    deleteJob,
    getTopicStats,
    applyForJob,
    getUserAppliedJobs,
    getUserCreatedJobs,
    getCandidatesPerJob,
)
from account.views import register, current_user, update_user, uploadResume

# Build in
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Jobs
    path("api/jobs/", getJobs, name="jobs"),
    path("api/jobs/<str:id>/", getJob, name="job"),
    path("api/jobs/new", createJob, name="create-job"),
    path("api/jobs/update/<str:id>/", updateJob, name="update-job"),
    path("api/jobs/delete/<str:id>/", deleteJob, name="delete-job"),
    path("api/jobs-by-user/", getUserCreatedJobs, name="jobs-by-user"),
    # Stats
    path("api/stats/<str:topic>/", getTopicStats, name="jobs-by-topic"),
    # Auth
    path("api/auth/register", register, name="register"),
    # Build in LOGIN functionality. Response sends access and refresh tokens
    path("api/auth/token", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("api/token/verify", TokenVerifyView.as_view()),
    path("api/me/", current_user, name="current-user"),
    path("api/auth/update", update_user, name="update-user"),
    # Resume
    path("api/upload/resume", uploadResume, name="upload-resume"),
    # Candidate
    path(
        "api/candidate/user-candidate-jobs/",
        getUserAppliedJobs,
        name="user-candidate-jobs",
    ),
    path(
        "api/candidate/job-candidates/<str:job_id>",
        getCandidatesPerJob,
        name="job-candidates",
    ),
    path("api/candidate/apply/<str:job_id>", applyForJob, name="apply-job"),
]

# Custom error handling. To rewrite default error response
handler500 = "utils.error_views.handler500"
handler404 = "utils.error_views.handler404"
