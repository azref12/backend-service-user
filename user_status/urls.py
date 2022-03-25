from rest_framework import routers
from django.urls import path
from user_status import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_status/', UserStatusList.as_view(queryset = user_status.objects.all(),
                                                 serializer_class = UserStatusSerializer)),
    path ('user_status/<int:pk>/', UserStatusDetail.as_view(queryset = user_status.objects.all(),
                                                            serializer_class = UserStatusSerializer))
]

urlpatterns += router.urls 