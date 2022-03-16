from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', include('user.urls')),
    path ('', include('user_detail.urls')),
    path ('', include('group.urls')),
    path ('', include('user_follow.urls')),
    path ('', include('user_like.urls')),
    path ('', include('user_recommended.urls')),
    path ('', include('user_status.urls')),
]
