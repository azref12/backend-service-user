from rest_framework import routers
from django.urls import path
from user_like import views
from user_like import view_like 
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_like/like_list/', views.like_list),
    path ('user_like/like_detail/<int:pk>/', views.like_detail),
    path ('user_like/', view_like.UserLikeList.as_view(queryset = user_like.objects.all(),
                                             serializer_class = UserLikeSerializer))
]

urlpatterns += router.urls 