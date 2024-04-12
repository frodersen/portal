from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response

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

