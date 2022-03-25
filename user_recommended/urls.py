from rest_framework import routers
from django.urls import path
from user_recommended import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_recommended/', RecommendedList.as_view(queryset = user_recommended.objects.all(),
                                                       serializer_class = UserRecommendedSerializer)),
    path ('user_recommended/<int:pk>/', RecommendedDetail.as_view(queryset = user_recommended.objects.all(),
                                                                  serializer_class = UserRecommendedSerializer))
]

urlpatterns += router.urls 