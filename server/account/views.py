from django.shortcuts import render
from .serializer import SignUpSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password


# Create your views here.
@api_view(["POST"])
def register(request):
    sign_up_serializer = SignUpSerializer(data=request.data)

    # check if email exists
    if User.objects.filter(email=request.data["email"]).exists():
        return Response(
            {"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Check if the serializer is valid
    if sign_up_serializer.is_valid():
        # Create a new user
        User.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            email=request.data["email"],
            password=make_password(request.data["password"]),
            username=request.data["username"],
        )
        return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)
    else:
        return Response(sign_up_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
# Check if the user is authenticated
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
