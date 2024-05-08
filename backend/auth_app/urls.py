from django.urls import path
from .views import LoginView, LogoutView, VerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Setup the schema view with drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Authentication API",
      default_version='v1',
      description="API documentation for authentication endpoints",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=()
)

urlpatterns = [
    # Endpoint for user login. Expects credentials and returns a JWT in an HTTP-only cookie.
    path('login/', LoginView.as_view(), name='login'),
    
    # Endpoint for user logout. Clears the HTTP-only cookie.
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Endpoint for JWT verification. Validates the JWT provided in the HTTP-only cookie.
    path('verify/', VerifyView.as_view(), name='verify'),
    
    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
