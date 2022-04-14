from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('user/user_list/', views.User_list),
    path ('user/user_detail/<int:pk>/', views.Users_details)
]