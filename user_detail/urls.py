from rest_framework import routers
from django.urls import path
from user_detail import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_detail/user_listing/', views.user_listing),
    path ('user_detail/UserDetails/<int:pk>/', views.UserDetails, name='UserDetails')
]

urlpatterns += router.urls