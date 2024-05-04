from rest_framework import serializers
from .models import Job, CandidatesApplied


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class CandidatesAppliedSerializer(serializers.ModelSerializer):
    # If not specifing job in response you will get only foreign key of job
    # doing like bellow you will get complete job object in response
    job = JobSerializer()

    class Meta:
        model = CandidatesApplied
        fields = "__all__"
        fields = ["user", "resume", "appliedAt", "job"]


# The JobSerializer class is a subclass of ModelSerializer,
# which is a serializer provided by Django REST Framework
# specifically designed to work with Django models.
# By subclassing ModelSerializer, we can automatically generate
# a serializer that maps all the fields of the Job model.

# The Meta class within the JobSerializer class is used to
# provide metadata about the serializer. In this case, it
# specifies the model that the serializer is based on,
# which is the Job model. The model attribute is set to Job,
# indicating that this serializer is used to serialize and deserialize instances of the Job model.

# The fields attribute is set to '__all__', which is a
# special value that tells the serializer to include all
# fields from the model in the serialized representation.
# This means that when an instance of the Job model is serialized
# using this serializer, all fields of the model will be
# included in the resulting JSON or other content type.

# By defining the JobSerializer class in this way, we can easily
# convert instances of the Job model into a format that can be
# transmitted over the web or stored in a database.
