from rest_framework import routers
from django.urls import path
from user_recommended import views
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_recommended/recommended_list/', views.recommended_list),
    path ('user_recommended/recommended_detail/<int:pk>/', views.recommended_detail)
]

urlpatterns += router.urls 