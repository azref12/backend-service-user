from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

urlpatterns = [ 
    path ('admin/', admin.site.urls),
    path ('auth/', include('auths.urls')),
    path ('', include('user.urls')),
    path ('', include('user_detail.urls')),
    path ('', include('group.urls')),
    path ('', include('user_follow.urls')),
    path ('', include('user_like.urls')),
    path ('', include('user_recommended.urls')),
    path ('', include('user_status.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
