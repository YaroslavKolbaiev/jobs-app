from rest_framework.views import exception_handler


def custom_exception_handler(exec, context):
    response = exception_handler(exec, context)

    # Retrieves the name of the exception class that was raised.
    exeption_class = exec.__class__.__name__

    print("EXCEPTION:", exeption_class)

    if response is not None:
        if exeption_class == "AuthenticationFailed":
            response.data = {"error": "Invalid email or password. Please try again"}
        if exeption_class == "NotAuthenticated":
            response.data = {
                "error": "You are not authenticated. Please go to login page"
            }
        if exeption_class == "InvalidToken":
            response.data = {"error": "Your session is expired. Please login again"}

    return response
