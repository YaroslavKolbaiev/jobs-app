from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
        ]  # fields to be serialized

        # extra_kwargs is used to specify additional validation for the fields
        extra_kwargs = {
            "username": {"required": True, "allow_blank": False},
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
            "email": {"required": True, "allow_blank": False},
            "password": {
                "write_only": True,
                "required": True,
                "allow_blank": False,
                "min_length": 6,
            },
        }


class UserSerializer(serializers.ModelSerializer):
    # Defining resume as a additional field in User Model. source is a referencing to UserProfile model field
    resume = serializers.CharField(source="userprofile.resume", required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "resume"]
