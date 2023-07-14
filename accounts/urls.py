from django.urls import path
from . import views
from .views import get_csrf_token

app_name = 'accounts'

urlpatterns = [
    path(r'signup/', views.signup_view, name="signup"),
    path(r'login/', views.login_view, name="login"),
    path(r'login/get_csrf_token/', views.get_csrf_token, name="token"),
    path(r'logout/', views.logout_view, name="logout")
]