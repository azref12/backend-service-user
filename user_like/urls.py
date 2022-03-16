from rest_framework import routers
from django.urls import path
from user_like import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_like/like_list/', views.like_list),
    path ('user_like/like_detail/<int:pk>/', views.like_detail)
]

urlpatterns += router.urls 