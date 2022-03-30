from rest_framework import routers
from django.urls import path
from user_follow import views
from user_follow import view_follow
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_follow/follow_list/', views.follow_list),
    path ('user_follow/follow_detail/<int:pk>/', views.follow_detail),
    path ('user_follow/', view_follow.FollowList.as_view(queryset = user_follow.objects.all(),
                                             serializer_class = FollowSerializer))
]

urlpatterns += router.urls  