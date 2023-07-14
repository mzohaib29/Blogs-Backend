from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),   # Raw string
    path(r'accounts/', include('accounts.urls')),
    path(r'articles/', include('articles.urls')),
    path(r'newapi/', include('newapi.urls')),
    path(r'about/', views.About),
    path(r'', views.Home)
]

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)