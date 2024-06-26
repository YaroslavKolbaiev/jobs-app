from .validators import validate_file_extension
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializer import SignUpSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .decorators import authorized_only
from .notification_manager import NotificationManager


# Create your views here.
@api_view(["POST"])
def register(request):
    sign_up_serializer = SignUpSerializer(data=request.data)

    # check if email exists
    if User.objects.filter(email=request.data["email"]).exists():
        return Response(
            {"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=request.data["username"]).exists():
        return Response(
            {"message": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST
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


@api_view(["POST"])
def login(request):
    data = request.data
    email = data.get("email")
    password = data.get("password")

    user = get_object_or_404(User, email=email)

    if not user.check_password(password):
        return Response(
            {"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST
        )

    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)

    serializer = UserSerializer(user)

    response = Response(
        {"data": serializer.data, "access_token": str(access)},
        status=status.HTTP_200_OK,
    )

    # Set the cookie
    response.set_cookie(
        "refresh_token", str(refresh), max_age=60 * 60 * 24 * 3, httponly=True
    )
    return response


@api_view(["GET"])
# Check if the user is authenticated
# @permission_classes([IsAuthenticated])
@authorized_only
def current_user(request):
    user = request.user
    access = AccessToken.for_user(user)
    serializer = UserSerializer(user)
    return Response(
        {"data": serializer.data, "access_token": str(access)},
        status=status.HTTP_200_OK,
    )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"data": serializer.data, "user_id": user.id}, status=status.HTTP_200_OK
        )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    user = request.user

    resume = request.FILES["resume"]

    if resume == "":
        return Response({"error": "Please upload your resume"}, status=404)

    is_valid_file = validate_file_extension(resume.name)

    if not is_valid_file:
        return Response(
            {"error": "Please upload only pdf, doc or docx files"}, status=404
        )

    resume.name = f"{user.id}_{resume.name}"

    serializer = UserSerializer(user)

    # In this case i cant just make serializer.save() like in previous example
    # because resume is not a field in User model. It is a field in UserProfile
    # model and serializer meta is defined for User model not for UserProfile

    user.userprofile.resume = resume
    user.userprofile.save()
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    response = Response({"message": "Logged out"}, status=status.HTTP_200_OK)
    response.delete_cookie("refresh_token")
    return response


@api_view(["POST"])
def send_message(request):
    request_data = request.data

    notification_manager = NotificationManager()

    notification_manager.send_msg(**request_data)

    return Response({"message": "Message sent"}, status=status.HTTP_200_OK)
