from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(r'', views.apiOverview , name="api"),
    path(r'task-list/', views.taskList , name="List"),
    path(r'task-create/', views.createTask, name="create")
]