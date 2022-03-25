from rest_framework import routers
from django.urls import path
from user_like import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_like/', UserLikeList.as_view(queryset = user_like.objects.all(),
                                             serializer_class = UserLikeSerializer)),
    path ('user_like/<int:pk>/', UserLikeDetail.as_view(queryset = user_like.objects.all(),
                                                        serializer_class = UserLikeSerializer))
]

urlpatterns += router.urls 