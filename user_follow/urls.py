from rest_framework import routers
from django.urls import path
from user_follow import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_follow/follow_list/', views.follow_list),
    path ('user_follow/follow_detail/<int:pk>/', views.follow_detail)
]

urlpatterns += router.urls