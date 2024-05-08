import logging
from rest_framework import views, status
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import JsonResponse
from django.conf import settings
from django.core.signing import Signer
import json
import urllib.parse
from django.http import HttpResponse
import base64

logger = logging.getLogger(__name__)

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        payload = {
            'phone_number': phone_number,
            'password': password,
        }

        response = requests.post(
            f'{settings.NTNUI_DEV_API_URL}/token/',
            data=payload,
        )
        logger.info(f"Login attempt for : {phone_number}")

        # Bad request
        if response.status_code == 400:
            logger.warning(response.json())
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

        # Unauthorized
        if response.status_code == 401:
            logger.warning(f"Unauthorized login attempt for : {phone_number}")
            return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED) 

        # Ok
        if response.status_code == 200:
            logger.info(f"Successful login : {phone_number}")
            # Create cookie with token av value
            access_token = response.json()['access']
            
            
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
            
        # Log unexpected server responses
        logger.error(f"Unexpected response for phone number {phone_number}: {response.status_code}")
        return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        response = HttpResponse("Logged out")
        response.delete_cookie('access_token')
        return response

class VerifyView(views.APIView):
        def post(self, request, *args, **kwargs):
            accessToken = cookies = request.COOKIES.get('access_token')
            
            if (not accessToken):
                logger.error(f"No token were given.")
                return Response({"detail": "No token given."}, status=status.HTTP_400_BAD_REQUEST)

            payload = {
            'token': accessToken,
            }

            response = requests.post(
            f'{settings.NTNUI_DEV_API_URL}/token/verify/',
            data=payload,
            )

            # Invalid token
            if (response.status_code == 401):
                logger.info(response.json())
                return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED) 

            if (response.status_code == 200):
                logger.info(response.json())
                return Response(response.json(), status=status.HTTP_200_OK) 

            # Log unexpected server responses
            logger.error(f"Unexpected error when validating token: {response.status_code}")
            return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)