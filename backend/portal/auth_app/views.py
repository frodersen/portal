from venv import logger
from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from rest_framework import status, views
from rest_framework.response import Response
import logging


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        # Prepare the payload for the API request
        payload = {
            'phone_number': phone_number,
            'password': password,
        }

        # Make the POST request to NTNUI API
        response = requests.post(
            f'{settings.NTNUI_API_URL}/token/',
            data=payload,
        )

        # Check if the response is successful
        if response.status_code == 200:
            # Here you'd handle the response and create a session
            # or a token that your system can use for SSO.
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            # Handle failed authentication
            return Response(response.json(), status=response.status_code)


import logging
from rest_framework import views, status
from rest_framework.response import Response
import requests
from django.conf import settings

class UserView(views.APIView):
    authentication_classes = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    def get(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        self.logger.debug(f'Received Authorization Header: {auth_header}')

        if not auth_header.startswith('Bearer '):
            return Response({"error": "Invalid or missing Authorization header"}, status=status.HTTP_401_UNAUTHORIZED)

        response = requests.get(
            f'{settings.NTNUI_API_URL}/users/profile',
            headers={'Authorization': auth_header}
        )

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 401:
            return Response("Invalid or expired token", status=status.HTTP_401_UNAUTHORIZED)
        else:
            self.logger.error(f"Failed to retrieve user profile: {response.status_code} - {response.text}")
            return Response("An error occurred when retrieving user data", status=response.status_code)
