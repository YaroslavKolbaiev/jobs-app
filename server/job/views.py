from django.shortcuts import get_object_or_404
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Max, Min, Avg


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
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


# Create get post by id.
@api_view(["GET"])
def getJob(request, id):
    # This line retrieves the Job object with the specified id from the database,
    # or raises a 404 Not Found error if no such object exists.
    job = get_object_or_404(Job, id=id)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createJob(request):
    data = request.data
    # **data is used to unpack the data dictionary into keyword arguments
    # similar to spread operator in JavaScript.
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteJob(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return Response({"message": "Job deleted successfully"}, status=204)


@api_view(["PUT"])
def updateJob(request, id):
    data = request.data
    job = get_object_or_404(Job, id=id)
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
