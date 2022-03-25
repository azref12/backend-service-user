from rest_framework import routers
from django.urls import path
from group import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('group/', GroupList.as_view(queryset=group.objects.all(), serializer_class=GroupSerializer)),
    path ('group/<int:pk>/', GroupDetail.as_view(queryset=group.objects.all(), serializer_class=GroupSerializer))
]

urlpatterns += router.urls 