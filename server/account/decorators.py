from functools import wraps
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import User


def authorized_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        cookies = request.COOKIES
        refresh_token = cookies.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            payload = UntypedToken(token=refresh_token).payload
            user_id = payload["user_id"]
            user = User.objects.get(id=user_id)
            request.user = user
        except (InvalidToken, TokenError) as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        return func(*args, **kwargs)

    return wrapper
