from rest_framework import routers
from django.urls import path
from user_detail import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_detail/', UserDetailList.as_view(queryset=user_detail.objects.all(), serializer_class=UserDetailSerializer)),
    path ('user_detail/<int:pk>/', UserDetailView.as_view(queryset=user_detail.objects.all(), serializer_class=UserDetailSerializer))
]
 
urlpatterns += router.urls