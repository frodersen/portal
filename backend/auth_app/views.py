import logging
from rest_framework import views, status
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import HttpResponse
from .api_specs import login_schema, logout_schema, verify_schema

# Setting up logging for the module
logger = logging.getLogger(__name__)

class LoginView(views.APIView):
    @login_schema
    def post(self, request, *args, **kwargs):
        # Extracting phone number and password from the POST request data
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        # Creating payload for authentication request
        payload = {
            'phone_number': phone_number,
            'password': password,
        }

        # Sending the authentication request to the external service
        response = requests.post(
            f'{settings.NTNUI_DEV_API_URL}/token/',
            data=payload,
        )
        # Log the login attempt
        logger.info(f"Login attempt for: {phone_number}")

        # Handle responses based on status codes
        if response.status_code == 400:
            # Log and respond with bad request information
            logger.warning(response.json())
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

        if response.status_code == 401:
            # Log and respond with unauthorized access information
            logger.warning(f"Unauthorized login attempt for: {phone_number}")
            return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)

        if response.status_code == 200:
            # Successful authentication
            logger.info(f"Successful login: {phone_number}")
            access_token = response.json()['access']
            
            # Create and send cookie with the access token
            cookie_response = Response(access_token, status=status.HTTP_200_OK)
            cookie_response.set_cookie(
                'access_token',
                max_age=3600,
                value=access_token,
                httponly=True,
                secure=True,
                samesite="Lax",
                # domain='.ntnui.no'
            )
            return cookie_response

        # Handle unexpected server errors
        logger.error(f"Unexpected response for phone number {phone_number}: {response.status_code}")
        return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(views.APIView):
    @logout_schema
    def post(self, request, *args, **kwargs):
        # Clear the access token cookie and return a logout message
        response = HttpResponse("Logged out")
        response.delete_cookie('access_token')
        return response

class VerifyView(views.APIView):
    @verify_schema
    def post(self, request, *args, **kwargs):
        # Retrieve the access token from the cookie
        accessToken = request.COOKIES.get('access_token')
        
        if not accessToken:
            # Log and return an error if no token is provided
            logger.error("No token provided.")
            return Response({"detail": "No token given."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare payload for token verification
        payload = {'token': accessToken}

        # Send request to verify the token
        response = requests.post(
            f'{settings.NTNUI_DEV_API_URL}/token/verify/',
            data=payload,
        )

        if response.status_code == 401:
            # Handle invalid token scenario
            logger.info(response.json())
            return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)

        if response.status_code == 200:
            # Token is valid
            logger.info(response.json())
            return Response(response.json(), status=status.HTTP_200_OK)

        # Log and handle unexpected errors during token validation
        logger.error(f"Unexpected error when validating token: {response.status_code}")
        return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
