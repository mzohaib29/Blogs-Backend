from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from .views import UserRegistrationView

urlpatterns = [
    path('', views.getRoutes),
    path("auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('signup/', UserRegistrationView.as_view(), name="signup"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]