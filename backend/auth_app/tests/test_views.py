from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
import json

# Unit tests for the authentication views
class AuthenticationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.verify_url = reverse('verify')

    @patch('requests.post')
    def test_login_success(self, mock_post):
        # Setup mock
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'access': 'fake_access_token'}

        # Test data
        data = {'phone_number': '1234567890', 'password': 'securepassword'}
        
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', self.client.cookies)

    @patch('requests.post')
    def test_login_failure(self, mock_post):
        # Setup mock for failed authentication
        mock_response = mock_post.return_value
        mock_response.status_code = 401
        mock_response.json.return_value = {'detail': 'Unauthorized'}

        data = {'phone_number': '1234567890', 'password': 'wrongpassword'}
        
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

