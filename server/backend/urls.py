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
    get_jobs,
    get_job,
    create_job,
    unpdate_job,
    delete_job,
    get_topic_stats,
    apply_for_job,
    get_user_applied_jobs,
    get_user_created_jobs,
    get_candidates_per_job,
)
from account.views import (
    register,
    current_user,
    update_user,
    upload_resume,
    login,
    logout,
    send_message,
)

# Build in
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Jobs
    path("api/jobs/", get_jobs, name="jobs"),
    path("api/jobs/<str:id>/", get_job, name="job"),
    path("api/jobs/new", create_job, name="create-job"),
    path("api/jobs/update/<str:id>/", unpdate_job, name="update-job"),
    path("api/jobs/delete/<str:id>/", delete_job, name="delete-job"),
    path("api/jobs-by-user/", get_user_created_jobs, name="jobs-by-user"),
    # Stats
    path("api/stats/<str:topic>/", get_topic_stats, name="jobs-by-topic"),
    # Auth
    path("api/auth/register", register, name="register"),
    # Build in LOGIN functionality. Response sends access and refresh tokens
    path("api/auth/token", login, name="token-obtain-pair"),
    path("api/token/verify", TokenVerifyView.as_view()),
    path("api/me/", current_user, name="current-user"),
    path("api/auth/update", update_user, name="update-user"),
    path("api/auth/logout", logout, name="logout"),
    path("api/send-message", send_message, name="send-message"),
    # Resume
    path("api/upload/resume", upload_resume, name="upload-resume"),
    # Candidate
    path(
        "api/candidate/user-candidate-jobs/",
        get_user_applied_jobs,
        name="user-candidate-jobs",
    ),
    path(
        "api/candidate/job-candidates/<str:job_id>",
        get_candidates_per_job,
        name="job-candidates",
    ),
    path("api/candidate/apply/<str:job_id>", apply_for_job, name="apply-job"),
]

# Custom error handling. To rewrite default error response
handler500 = "utils.error_views.handler500"
handler404 = "utils.error_views.handler404"
