from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Job, CandidatesApplied
from .serializers import JobSerializer, CandidatesAppliedSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Count, Max, Min, Avg
from .filters import JobsFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

JOBS_PER_PAGE = 2


@api_view(["GET"])
def getTopicStats(request, topic):
    # This line is responsible for querying the database to retrieve
    # a list of Job objects that have a title containing a specific topic.
    jobs = Job.objects.filter(title__icontains=topic)
    if len(jobs) == 0:
        return Response({"message": f"No job found for {topic}"}, status=404)

    stats = jobs.aggregate(
        total_jobs=Count("title"),  # Count the number of jobs
        avg_positions=Avg("position"),  # Calculate the average position
        avg_salary=Avg("salary"),  # Calculate the average salary
        min_salary=Min("salary"),  # Calculate the minimum salary
        max_salary=Max("salary"),  # Calculate the maximum salary
    )

    return Response(stats)


# Create get all posts.
@api_view(["GET"])
def getJobs(request):
    # This line is responsible for filtering the Job objects based on the query parameters.
    filterset = JobsFilter(
        request.GET, queryset=Job.objects.all().order_by("-created_at")
    )
    # Total number of jobs
    total_jobs = filterset.qs.count()
    # This line is responsible for paginating the filtered queryset.
    paginator = PageNumberPagination()
    # Set the number of jobs per page.
    paginator.page_size = JOBS_PER_PAGE
    # Paginate the queryset. To specify page number client has include page param in request
    queryset = paginator.paginate_queryset(filterset.qs, request)
    # filterset.qs is the filtered queryset.
    serializer = JobSerializer(queryset, many=True)
    return Response(
        {
            "jobs": serializer.data,
            "total_jobs": total_jobs,
            "jobs_per_page": JOBS_PER_PAGE,
        }
    )


@api_view(["GET"])
def getJob(request, id):
    # This line retrieves the Job object with the specified id from the database,
    # or raises a 404 Not Found error if no such object exists.
    job = get_object_or_404(Job, id=id)
    candidates = CandidatesApplied.objects.filter(job=id).count()
    serializer = JobSerializer(job, many=False)
    return Response({"job": serializer.data, "candidates": candidates})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserCreatedJobs(request):
    kwargs = {"user": request.user.id}
    jobs = Job.objects.filter(**kwargs)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createJob(request):
    request.data["user"] = request.user
    data = request.data
    # **data is used to unpack the data dictionary into keyword arguments
    # similar to spread operator in JavaScript.
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def applyForJob(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    user = request.user

    # Check if resume is provided
    if user.userprofile.resume == "":
        return Response(
            {"error": "Please upload your resume first"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Check if job date is still valid
    if job.lastDate < timezone.now():
        return Response(
            {"error": "You not allowed to apply this job. Date is over"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Check if the user has already applied for the job
    if CandidatesApplied.objects.filter(job=job, user=user).exists():
        return Response(
            {"error": "You have already applied for this job"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    candidate = CandidatesApplied.objects.create(
        job=job,
        user=user,
        resume=user.userprofile.resume,
    )

    serializer = CandidatesAppliedSerializer(candidate, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserAppliedJobs(request):
    user = request.user

    jobs_applied = CandidatesApplied.objects.filter(user=user.id)

    serializer = CandidatesAppliedSerializer(jobs_applied, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCandidatesPerJob(request, job_id):
    current_job = get_object_or_404(Job, id=job_id)

    if current_job.user != request.user:
        return Response(
            {"error": "You are not allowed to access data of current job"},
            status=status.HTTP_403_FORBIDDEN,
        )

    candidates = CandidatesApplied.objects.filter(job=job_id)
    serializer = CandidatesAppliedSerializer(candidates, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteJob(request, id):
    job = get_object_or_404(Job, id=id)
    # Allow to update job only for the user who created the job
    if job.user != request.user:
        return Response(
            {"message": "You are not authorized to update this job"},
            status=status.HTTP_403_FORBIDDEN,
        )
    job.delete()
    return Response(
        {"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateJob(request, id):
    data = request.data
    job = get_object_or_404(Job, id=id)

    # Allow to update job only for the user who created the job
    if job.user != request.user:
        return Response(
            {"message": "You are not authorized to update this job"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = JobSerializer(instance=job, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# ----------------- Old way of updating job -----------------
# @api_view(["PUT"])
# def updateJob(request, id):
#     data = request.data
#     job = get_object_or_404(Job, id=id)

#     job.title = data["title"]
#     job.description = data["description"]
#     job.email = data["email"]
#     job.address = data["address"]
#     job.salary = data["salary"]
#     job.position = data["position"]
#     job.company = data["company"]
#     job.point = data["point"]
#     job.lastDate = data["lastDate"]
#     job.user = data["user"]
#     job.jobType = data["jobType"]
#     job.education = data["education"]
#     job.industry = data["industry"]
#     job.experience = data["experience"]

#     serializer = JobSerializer(job, many=False)

#     return Response(serializer.data)
