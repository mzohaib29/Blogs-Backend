from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [     
    path(r'', views.article_list, name="list"),     # Raw string
    path(r'get/<id>/', views.article_one, name="getById"),
    path(r'create/', views.article_create, name = "create"),
    path(r'update/<id>/', views.article_update, name="update"),
    path(r'delete/<id>/', views.article_delete, name="delete"),
    path(r'<slug:slug>/', views.article_detail, name="details"),
]
