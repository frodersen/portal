from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import VerifyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', VerifyView.as_view(), name='verify')
]
