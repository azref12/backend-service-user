from rest_framework import routers
from django.urls import path
from user_status import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_status/status_list/', views.status_list),
    path ('user_status/status_detail/<int:pk>/', views.status_detail)
]

urlpatterns += router.urls 