from django.urls import path
from .views import LoginView, LogoutView, VerifyView

# URL configurations for the authentication app.
urlpatterns = [
    # Endpoint for user login. Expects credentials and returns a JWT in an HTTP-only cookie.
    path('login/', LoginView.as_view(), name='login'),
    
    # Endpoint for user logout. Clears the HTTP-only cookie.
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Endpoint for JWT verification. Validates the JWT provided in the HTTP-only cookie.
    path('verify/', VerifyView.as_view(), name='verify')
]
