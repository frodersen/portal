from django.urls import path
from .views import LoginView
from .views import UserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user-profile/', UserView.as_view(), name='user_profile_proxy'),
    # Add other authentication-related URLs here
]
