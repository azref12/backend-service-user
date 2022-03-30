from rest_framework import routers
from django.urls import path
from user_status import views
from user_status import view_status
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_status/status_list/', views.status_list, name='status_list'),
    path ('user_status/status_detail/<int:pk>/', views.status_detail, name='status_detail'),
    path ('user_status/', view_status.UserStatusList.as_view(queryset = user_status.objects.all(),
                                                       serializer_class = UserStatusSerializer))
]

urlpatterns += router.urls  