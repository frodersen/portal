from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Detailed Swagger auto schema for the LoginView
login_schema = swagger_auto_schema(
    operation_summary="Login",
    operation_description="Authenticate a user by their phone number and password.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['phone_number', 'password'],
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='User phone number'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
    ),
    responses={
        200: openapi.Response(description='Authentication successful, JWT provided in cookie'),
        400: openapi.Response(description='Bad request, wrong parameters'),
        401: openapi.Response(description='Unauthorized, wrong credentials'),
        500: openapi.Response(description='Internal server error')
    }
)

# Detailed Swagger auto schema for the LogoutView
logout_schema = swagger_auto_schema(
    operation_summary="Logout",
    operation_description="Log out a user by clearing the access token cookie.",
    responses={
        200: openapi.Response(description='Logout successful, cookie cleared'),
    }
)

# Detailed Swagger auto schema for the VerifyView
verify_schema = swagger_auto_schema(
    operation_summary="Verify Token",
    operation_description="Verifies the validity of the provided JWT token.",
    manual_parameters=[
        openapi.Parameter(
            name='access_token',
            in_='cookie',
            description='JWT access token provided in a cookie',
            type=openapi.TYPE_STRING,
            required=True
        )
    ],
    responses={
        200: openapi.Response(description='Token is valid'),
        400: openapi.Response(description='Token not provided or malformed'),
        401: openapi.Response(description='Invalid token, unauthorized access'),
        500: openapi.Response(description='Internal server error')
    }
)
