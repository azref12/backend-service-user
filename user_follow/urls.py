from rest_framework import routers
from django.urls import path
from user_follow import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_follow/', FollowList.as_view(queryset = user_follow.objects.all(),
                                             serializer_class = FollowSerializer)),
    path ('user_follow/<int:pk>/', FollowDetail.as_view(queryset = user_follow.objects.all(),
                                                        serializer_class = FollowSerializer))
]

urlpatterns += router.urls  