from rest_framework import routers
from django.urls import path
from group import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('group/group_list/', views.group_list),
    path ('group/group_detail/<int:pk>/', views.group_detail)
]

urlpatterns += router.urls 